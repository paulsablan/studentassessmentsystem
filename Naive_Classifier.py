from common import *
import fuzzy_logic

def train_naive(filename, split_ratio):
	labels, data, test = load_csv_section(filename, split_ratio)
	print(data)
	exit()
	# Data for Second Half Grade
	data_second_half = []
	test_second_half = []
	for i in data:
		j = i[0:-1]
		data_second_half.append(j)
	for i in test:
		j = i[0:-1]
		test_second_half.append(j)

	# Top 10 Pupils
	test_top_top = data[:]

	## prepare model
	# Summaries for second half
	results_second_half = []
	summaries_second_half = class_summarize(data_second_half)
	predictions = get_predictions(summaries_second_half, test_second_half)
	accuracy, score, error_analysis = get_accuracy(test_second_half, predictions)
	results_second_half.append(predictions)
	results_second_half.append(accuracy)
	results_second_half.append(score)
	results_second_half.append(error_analysis)
	print(('\n#Second Half\nAccuracy: {}%\nScore: {}/{}\nError Analysis: {}').format(accuracy,score,len(test_second_half),error_analysis))

	# Data for Final Grade
	data_final_grade = data[:]
	test_final_grade = test[:]
	for i in data_final_grade:
		for j in range(len(i)):
			i[-2] = predictions[j]

	#summaris for Final Grade
	summaries_final = class_summarize(data_final_grade)

	# Test Final grade
	results_final_grade = []
	predictions = get_predictions(summaries_final, test_final_grade)
	accuracy, score, error_analysis = get_accuracy(test_final_grade, predictions)
	results_final_grade.append(predictions)
	results_final_grade.append(accuracy)
	results_final_grade.append(score)
	results_final_grade.append(error_analysis)
	print(('\n#Final\nAccuracy: {}%\nScore: {}/{}\nError Analysis: {}').format(accuracy,score,len(test_second_half),error_analysis))
	print('\n')
	for i in range(len(labels[0])):
		print(('{} : {} : {}').format(i, labels[0][i], test[0][i]))

	#Fuzzy Inference System
	fuzzy_results = []
	fuzzy_financial = fis.financial_fuzzy(test[0][0], test[0][4], test[0][5])
	print("Financial ",fuzzy_financial)
	fuzzy_results.append(fuzzy_financial)

	fuzzy_family = fis.broken_family(test[0][1], test[0][7])
	print("Family ", fuzzy_family)
	fuzzy_results.append(fuzzy_family)

	fuzzy_relatives = fis.living_with_rel(test[0][1], test[0][7])
	print("Relatives", fuzzy_relatives)
	fuzzy_results.append(fuzzy_relatives)

	fuzzy_health = fis.health_conditions(test[0][10], test[0][8], test[0][11])
	print("Health", fuzzy_health)
	fuzzy_results.append(fuzzy_health)

	fuzzy_materials = fis.insufficient_learning_materials(test[0][9], test[0][4], test[0][5])
	print("Materials",fuzzy_materials)
	fuzzy_results.append(fuzzy_materials)

	fuzzy_parenting = fis.parenting_issues(test[0][1], test[0][2], test[0][3])
	print("Parenting", fuzzy_parenting)
	fuzzy_results.append(fuzzy_parenting)

	fuzzy_study_habit = fis.study_habit(test[0][8], test[0][11], test[0][6])
	print("Study Habit", fuzzy_study_habit)
	fuzzy_results.append(fuzzy_study_habit)

	return results_second_half, results_final_grade, fuzzy_results

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
		fuzzy_financial = fis.financial_fuzzy(d[0], d[4], d[5])

		fuzzy_family = fis.broken_family(d[1], d[7])

		fuzzy_relatives = fis.living_with_rel(d[1], d[7])

		fuzzy_health = fis.health_conditions(d[10], d[8], d[11])

		fuzzy_materials = fis.insufficient_learning_materials(d[9], d[4], d[5])

		fuzzy_parenting = fis.parenting_issues(d[1], d[2], d[3])

		fuzzy_study_habit = fis.study_habit(d[8], d[11], d[6])

		fuzzy_results.append([fuzzy_financial, fuzzy_family, fuzzy_relatives, fuzzy_health,
							fuzzy_materials, fuzzy_parenting, fuzzy_study_habit])
	return fuzzy_results

if __name__ == "__main__":
	args = parse_args(additional_args=[])
	# if args.retrain == 1:
	# 	filename = args.datasets+'/'+args.filename
	# 	train_naive(filename, args.splitratio)
	sum1, sum2 = get_summaries('./dataset/dataset_new.csv', 100)
	predictions = predict_grades('./dataset/STEM-12-7.csv', sum1, sum2, None)
	print(predictions)
	fuzzy_results = get_fuzzy_results('./dataset/STEM-12-7.csv', [2,1,2,3,1,1,0,2,2,1,2,4,83])
