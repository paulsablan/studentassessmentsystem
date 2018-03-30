from flask import Flask, request, render_template, jsonify
import json
import os
import smtplib
import base64
from email.mime.text import MIMEText
from Naive_Classifier import train_naive, get_summaries, predict_grades, get_fuzzy_results
from twilio.rest import Client

app = Flask(__name__)

SCOPES = 'https://www.googleapis.com/auth/gmail.send'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Send Email'
@app.route('/', methods=['GET'])
def index():
	
	return render_template('login.html')

@app.route('/home', methods=['POST'])
def login():
	role = ""
	page = ""

	if request.form['userId']=='admin' and request.form['password']=='admin':
    		role = "admin"
    		return render_template("Admin.html")
	elif request.form['userId']=='faculty' and request.form['password']=='faculty':
  			role = "faculty"
  			return render_template("Faculty.html")
	return jsonify(role = role)

@app.route('/sendemail/<string:receive>/<string:filename>/<string:dataset>', methods=['GET','POST'])
def sendemail(receive,filename,dataset):

	comp_path = os.getcwd();
	new_comp_path = '/'.join(comp_path.split('\\'))
	filepath = new_comp_path + "/defaultMessage.txt"
	file = new_comp_path + "/dataset/" + filename
	get_summaries_file = new_comp_path + "/dataset/dataset_new.csv"
	# Open a plain text file for reading.  For this example, assume that
	# the text file contains only ASCII characters.
	fp = open(filepath, 'r')
	# Create a text/plain message
	msg = MIMEText(fp.read())
	fp.close()
	textmsg = msg.as_string()
	print(textmsg)
	sender = 'studentassessmentsystem@gmail.com'
	password = 'studentperformancesystem'
	receiver = receive
	status = ""
	studentdata = dataset
	print(studentdata)
	#second_half,final_grade,fuzzy_results = train_naive(file,98)
	second_half, final_grade =  get_summaries(get_summaries_file,100)
	predict_secondhalf, predict_finalgrade = predict_grades(file,second_half, final_grade,None)
	fuzzy_results =  get_fuzzy_results(file)
	print(second_half)
	print(final_grade)
	print(predict_secondhalf)
	print(predict_finalgrade)
	print(fuzzy_results)

	# me == the sender's email address
	# you == the recipient's email address
	msg['Subject'] = 'This message is about the status of your child for this school year'
	msg['From'] = sender
	msg['To'] = receiver
	# Find these values at https://twilio.com/user/account
	account_sid = "AC58613e0ef906d4a1077f2d98df3b0a9a"
	auth_token = "374f6acea8826186eee9ac522afd0764"
	client = Client(account_sid, auth_token)
	# client.api.account.messages.create(
	#     to="+639162438998",
	#     from_="+15138135511",
	#     body=textmsg)
	# Send the message via our own SMTP server, but don't include the
	# envelope header.
	s = smtplib.SMTP(host='smtp.gmail.com', port=587)
	s.starttls()
	s.login(sender,password)
	s.sendmail(sender, receiver, msg.as_string())
	s.quit()
	status = "sent"
	return jsonify(status = status, predict_secondhalf = predict_secondhalf ,predict_finalgrade = predict_finalgrade, fuzzy_results = fuzzy_results)

if __name__ == "__main__":	
	app.run(debug=True,host='0.0.0.0', port=80)
 