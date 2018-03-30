import argparse
import random
import csv
import math
import random

from utils import *

alpha = 1.0

def parse_args(additional_args=[]):
	parser = argparse.ArgumentParser()

	#Defaults
	parser.add_argument('--splitratio', type=int, default=90)
	parser.add_argument('--datasets', type=str, default='./dataset')
	parser.add_argument('--filename', type=str, default='STEM-12-7.csv')
	# parser.add_argument('--filename', type=str, default='student-mat.csv')
	parser.add_argument('--retrain', type=int, default=1)

	#Additional Args
	for key, kwargs in additional_args:
		parser.add_argument(key, **kwargs)

	args = parser.parse_args()

	return args
def load_csv_section(filename, splitratio):
	xs = []
	ys = []
	lines = csv.reader(open(filename, "r"))
	dataset = list(lines)
	population = len(dataset)
	limit = int(population - (((100 - splitratio) / 100) * population))
	for i in range(len(dataset)):
		for j in dataset[i]:
			data = j.split(',')
			if i == 0:
				ys.append(data)
			else:
				xs.append(data[2:])
				xs[-1] = convert_to_int(xs[-1])
	# for i in range(len(dataset)):
	# 	if i == 0:
	# 		ys = dataset[i]
	# 	else:
	# 		j = dataset[i][2:]
	# 		xs.append(j)
	# 		xs[-1] = convert_to_int(xs[-1])
	return ys, xs[0:limit], None

def load_csv_clean(filename, splitratio):
	ys = []
	xs = []
	lines = csv.reader(open(filename, "r"))
	dataset = list(lines)
	population = len(dataset)
	index = [x for x in range(population)]
	random.shuffle(index)
	limit = int(population - (((100 - splitratio) / 100) * population))
	for i in index:
		if i == 0:
			ys.append(dataset[i])
		else:
			xs.append(dataset[i])
			xs[-1] = convert_to_int(xs[-1])

	return ys, xs[0:limit], xs[limit+1:-1]

def load_csv_unclean(filename, splitratio):
	ys = []
	xs = []
	lines = csv.reader(open(filename, "r"))
	dataset = list(lines)
	population = len(dataset)
	index = [x for x in range(population)]
	random.shuffle(index)
	limit = int(population - (((100 - splitratio) / 100) * population))

	for i in index: #dataset[i]
		for j in dataset[i]:
			data = j.split(';')
			if i == 0:
				ys.append(data)
				ys = transform_dataset(ys)[0]
			else:
				xs.append(data)

	xs = transform_dataset(xs)
	xs = convert_values(xs)

	myFile = open('./dataset/dataset.csv', 'w', newline='')
	with myFile:
		data = []
		data.append(ys)
		for i in range(len(xs)):
			data.append(xs[i])
		writer = csv.writer(myFile)
		writer.writerows(data)

	return ys, xs[0:limit], xs[limit+1:-1]

def transform_dataset(data):
	new_data = []
	for i in data:
		del i[27]
		del i[26]
		del i[25]
		del i[24]
		del i[23]
		del i[22]
		del i[20]
		del i[19]
		del i[17]
		del i[15]
		del i[13]
		del i[12]
		del i[11]
		del i[10]
		del i[3]
		del i[2]
		del i[1]
		del i[0]
		new_data.append(i)
	return new_data

def get_classes(dataset):
	separated = {}
	for i in range(len(dataset)):
		vector = dataset[i]
		if (vector[-1] not in separated):
			separated[vector[-1]] = []
		separated[vector[-1]].append(vector)
	return separated

def get_mean(data):
	return sum(data) / float(len(data))

def get_stdev(data):
	avg = get_mean(data)
	pop_size = len(data	)
	# pop_size = len(data)-1
	# if pop_size <= 0:
	# 	pop_size = len(data)
	variance = sum([pow(x-avg,2) for x in data]) / float(pop_size)
	return math.sqrt(variance)

def summarize(dataset):
	summaries = []
	for attribute in zip(*dataset):
		summaries.append([get_mean(attribute), get_stdev(attribute)])
	del summaries[-1]
	return summaries

def class_summarize(data):
	summaries = {}
	separated = get_classes(data)
	for class_value, instances in separated.items():
		summaries[class_value] = summarize(instances)
	return summaries

def calculate_probability(x, mean, stdev):
	if stdev == 0:
		stdev = 1
	exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
	return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent

def calculate_class_probabilities(summaries, input_vector):
	# print((input_vector))
	probabilities = {}
	for class_value, class_summaries in summaries.items():
		probabilities[class_value] = 1
		for i in range(len(class_summaries)):
			mean, stdev = class_summaries[i]
			x = input_vector[i]
			probabilities[class_value] *= calculate_probability(x, mean, stdev)
	return probabilities

def predict(summaries, input_vector):
	probabilities = calculate_class_probabilities(summaries, input_vector)
	best_label, best_prob = None, -1
	for class_value, probability in probabilities.items():
		if best_label is None or probability > best_prob:
			best_prob = probability
			best_label = class_value
	return best_label

def get_predictions(summaries, test_set):
	predictions = []
	for i in range(len(test_set)):
		result = predict(summaries, test_set[i])
		predictions.append(result)
	return predictions

def get_accuracy(test_set, predictions):
	correct = 0
	error_analysis = []
	for x in range(len(test_set)):
		#Score
		if test_set[x][-1] == predictions[x]:
			correct += 1
		#Error Analysis
		true_val = test_set[x][-1]
		if true_val == 0:
			true_val = 10
			predictions[x] += 10
		er =( (abs(true_val - predictions[x])) / true_val ) * 100
		error_analysis.append(er)
	er = 100 - (sum(error_analysis)/len(error_analysis))
	return (correct/float(len(test_set))) * 100.0, correct, er
