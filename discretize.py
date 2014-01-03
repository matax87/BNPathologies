from dtmath import *
	
def generate_candidate_thresholds(values, classes):
	"Generate a list of candidate thresholds."
	thresholds = []
	pairs = sorted(zip(values, classes))
	for i in range(len(pairs) - 1):
		v1, c1 = pairs[i]
		v2, c2 = pairs[i + 1]
		if c1 != c2:
			a = (v1 + v2) / 2.0
			thresholds.append(a)	
	return thresholds
	
def binary_discretization(values, threshold):
	"Discretize the values in 'no'/'yes' based on the given threshold."
	return ['yes' if v >= threshold else 'no' for v in values];
	
def highest_threshold(values, classes):
	"""Computes the threshold producing the highest 'information gain'.
	It can be used to discretize the attribute."""
	thresholds = generate_candidate_thresholds(values, classes)
	highest_t = max(thresholds, key=lambda t: info_gain(binary_discretization(values, t), classes))
	return highest_t
	
def highest_infogain_threshold(values, classes):
	"Computes the highest 'information gain' and the according threshold producing it."
	thresholds = generate_candidate_thresholds(values, classes)
	info_gains = [info_gain(binary_discretization(values, t), classes) for t in thresholds]
	highest = max(zip(info_gains, thresholds), key=lambda p: p[0])
	return highest
		
			
			
		