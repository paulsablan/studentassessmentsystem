import numpy as np
from common import *
np.set_printoptions(precision=6)

class MultinomialNB(object):
	def __init__(self, alpha=1):
		self.alpha = alpha

	def fit(self, X, y):
		count_sample = X.shape[0]
		separated = [[x for x, t in zip(X, y) if t == c] for c in np.unique(y)]
		self.class_log_prior_ = [np.log(len(i) / count_sample) for i in separated]
		count = np.array([np.array(i).sum(axis=0) for i in separated]) + self.alpha
		self.feature_log_prob_ = np.log(count / count.sum(axis=1)[np.newaxis].T)
		return self

	def predict_log_proba(self, X):
		return [(self.feature_log_prob_ * x).sum(axis=1) + self.class_log_prior_
				for x in X]

	def predict(self, X):
		return np.argmax(self.predict_log_proba(X), axis=1)


if __name__ == '__main__':
	args = parse_args(additional_args=[])
	filename = args.datasets+'/'+args.filename
	labels, data, test = load_csv(filename, args.splitratio)
	X = []
	y = []
	X_test = []
	y_test = []
	for i in range(len(data)):
		X.append(data[i][0:-1])
		y.append(data[i][-1])

	for i in range(len(test)):
		X_test.append(data[i][0:-1])
		y_test.append(data[i][-1])

	X = np.array(X)
	X_test = np.array(X_test)
	y = np.array(y)
	y_test = np.array(y_test)
	nb = MultinomialNB().fit(X, y)

	results = nb.predict(X_test)
	for i in range(len(X_test)):
		print(('{} : {}').format(y_test[i], results[i]))
