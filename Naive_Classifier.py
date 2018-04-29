from common import *
import fuzzy_logic

def get_summaries(filename, split_ratio):
	labels, data, test = load_csv_clean(filename, split_ratio)
	# Summaries for second half
	data_second_half = []
	for i in data:
		j = i[0:-1]
		data_second_half.append(j)

	data_final_grade = data[:]

	summaries_second_half = class_summarize(data_second_half)
	summaries_final = class_summarize(data_final_grade)

	return summaries_second_half, summaries_final

def predict_grades(filename, summaries_second_half, summaries_final, data=None):
	test_second_half = []
	test_final_grade = []
	passed = False

	if data is None:
		pass_by = False
		labels, data, test = load_csv_section(filename, 100)
		passed = True

	for i in data:
		test_second_half.append(i)
	for i in data:
		test_final_grade.append(i)

	if passed is not True:
		test_second_half = [test_second_half]
		test_final_grade = [test_final_grade]

	predictions_second_half = get_predictions(summaries_second_half, test_second_half)
	predictions = predictions_second_half[:]

	for i in range(len(predictions)):
		test_final_grade[i].append(predictions[i])

	predictions_final = get_predictions(summaries_final, test_final_grade)
	return predictions_second_half, predictions_final

def get_fuzzy_results(filename, data=None):
	if data is None:
		labels, data, test = load_csv_section(filename, 100)
	else:
		temp = data[:]
		data = []
		data.append(temp)
	#Fuzzy Inference System
	fis = fuzzy_logic.fis()
	fuzzy_results = []
	for d in data:
		fuzzy_family = fis.broken_family(d[0], d[3])
		fuzzy_financial = fis.financial_fuzzy(d[1], d[3])
		fuzzy_study_habit = fis.study_habit(d[2], d[3])
		print(fuzzy_family, fuzzy_financial, fuzzy_study_habit)
		fuzzy_results.append([fuzzy_financial, fuzzy_family, fuzzy_study_habit])
	return fuzzy_results

if __name__ == "__main__":
	args = parse_args(additional_args=[])
	# if args.retrain == 1:
	# 	filename = args.datasets+'/'+args.filename
	# 	train_naive(filename, args.splitratio)
	sum1, sum2 = get_summaries('./dataset/dataset_new_v2.csv', 100)
	predictions = predict_grades('./dataset/testing_set_v2.csv', sum1, sum2, None)
	# print(predictions)
	# write_results(predictions)
	fuzzy_results = get_fuzzy_results('./dataset/testing_set_v2.csv', None)
	# print(fuzzy_results)
	# write_results(fuzzy_results)
