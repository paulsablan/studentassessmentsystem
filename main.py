from flask import Flask, request, render_template, jsonify
import json
import os
import smtplib
import base64
from email.mime.text import MIMEText
from Naive_Classifier import train_naive, get_summaries, predict_grades, get_fuzzy_results
from twilio.rest import Client
import sqlite3 as sql
import cv2

app = Flask(__name__)

SCOPES = 'https://www.googleapis.com/auth/gmail.send'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Send Email'

@app.route('/', methods=['GET'])
def index():

	return render_template('login.html')

@app.route('/create', methods=['GET'])
def create():
	return render_template('AddUser.html')

@app.route('/add',methods = ['POST', 'GET'])
def addrec():
	if request.method == 'POST':
		try:
			fname = request.form['fName']
			lname = request.form['lName']
			username = request.form['uName']
			password = request.form['pWord']
			role =  request.form['role']
			# Paul pacheck if nakukuha yung image file from form

			# image = file.data
			# print("image", image)
			# # image_filename = secure_filename(image.filename)
			# image_filename = image.filename
			# extension = image_filename.rsplit('.', 1)[1].lower()
			# # image_hashed_filename = str(uuid.uuid4().hex) + '.' + extension
			# file_path = os.path.join('/static/images/', file)
			
			# image.save(file_path)
			
			# comp_path = os.getcwd();
			# new_comp_path = '/'.join(comp_path.split('\\'))
			# print(file)
			# imagefile = new_comp_path + "/static/images/" + file
			# print(imagefile)
			# shutil.copyfile(file, imagefile)
			
			with sql.connect("database.db") as con:
				print(fname,lname,username,password,role)
				cur = con.cursor()
				cur.execute('INSERT INTO users (fname,lname,username,password,role) VALUES (?,?,?,?,?)',(fname,lname,username,password,role) )

				con.commit()
				cur.execute('SELECT * FROM users')
				rows = cur.fetchall();
				print(rows)				
				msg = "Record successfully added"
				print(msg)
		except:
			con.rollback()
			msg = "error in insert operation"
	  
		finally:
			con.close()

	# print(image)
	# img = cv2.imread(image, 1)
	# extension = image.rsplit('.', 1)[1].lower()
	# cv2.imwrite(os.path.join("/static/images/profiles/" , username + extension),img)
	# cv2.waitKey(0)
	return render_template("list.html",msg = msg,rows =rows)

@app.route('/home', methods=['POST'])
def login():
	role = ""
	user = request.form['userId']
	pword = request.form['password']

	try:
		with sql.connect("database.db") as con:
			cur = con.cursor()
			statement = cur.execute('SELECT * FROM users WHERE username = ? AND password = ?', [(user),(pword)])
			results = cur.fetchall()
			print(results)
			if results:
				role_statement = cur.execute('SELECT role FROM users WHERE username = ? AND password = ?', [(user),(pword)])
				role = str(cur.fetchone()[0])
				fname_statement = cur.execute('SELECT fname FROM users WHERE username = ? AND password = ?', [(user),(pword)])
				fname = str(cur.fetchone()[0])
				lname_statement = cur.execute('SELECT lname FROM users WHERE username = ? AND password = ?', [(user),(pword)])
				lname = str(cur.fetchone()[0])
				print(fname,lname)
				if role == "Faculty":
					return render_template("Faculty.html",fname = fname,lname = lname)
				elif role == "Admin":
					return render_template("Admin.html",fname = fname,lname = lname)
			else:
				print("Incorrect username or password! If you are not a user, please register here.")
	except IOError:
		print ("Select statement could not execute!")
	finally:
		con.close()

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
	print(type(studentdata))
	print(studentdata)
	if type(studentdata) is str and (studentdata == "None" or studentdata == ",,,,,,,,,,,,,,"):
		studentdata = None
	else:
		j = studentdata.split(',')
		studentdata = []
		for i in range(2,len(j)):
			studentdata.append(int(j[i]))
			
	#second_half,final_grade,fuzzy_results = train_naive(file,98)
	second_half, final_grade =  get_summaries(get_summaries_file,100)
	predict_secondhalf, predict_finalgrade = predict_grades(file,second_half, final_grade, studentdata)
	fuzzy_results =  get_fuzzy_results(file, studentdata)
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
	# s = smtplib.SMTP(host='smtp.gmail.com', port=587)
	# s.starttls()
	# s.login(sender,password)
	# s.sendmail(sender, receiver, msg.as_string())
	# s.quit()
	status = "sent"
	return jsonify(status = status, predict_secondhalf = predict_secondhalf ,predict_finalgrade = predict_finalgrade, fuzzy_results = fuzzy_results)

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0', port=80)
