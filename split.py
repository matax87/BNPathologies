import random
import numpy as np
	
def train_test_split(data, test_ratio):
	size = len(data)
	training_size = int(size * (1 - test_ratio))
	test_size = size - training_size
	random.shuffle(data)
	return data[:training_size], data[training_size:]
	
def train_test_prop_split(data, test_ratio, column_index):
	a = np.array(data)
	
	train = []
	test = []
	for x in set(a[:, column_index].tolist()):
		sub_a = a[a[:, column_index] == x]
		sub_a_train, sub_a_test = train_test_split(sub_a.tolist(), test_ratio)
		train.extend(sub_a_train)
		test.extend(sub_a_test)
	return train, test