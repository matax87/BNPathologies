import numpy as np
	
def frequencies(S):
	"Computes the dictionary of frequencies of an iterable object."
	from collections import defaultdict
	d = defaultdict(int)	
	for v in S:
		d[v] += 1	
	return d
	
def test_frequencies():
	f = frequencies([])
	assert(f['abc'] == 0)
	assert(f['def'] == 0)
	assert(f['zzz'] == 0)
	assert(f['test'] == 0)
	test = 'abc def abc def zzz'.split()
	f = frequencies(test)
	assert(f['abc'] == 2)
	assert(f['def'] == 2)
	assert(f['zzz'] == 1)
	assert(f['test'] == 0)
	
def information_entropy(S):
	"Computes the entropy of a collection of instances."
	h = 0
	f = frequencies(S)
	for v in S: 		
		p = f[v] / float(len(S))
		h += p * np.log2(p)
	return -h
	
def test_information_entropy():
	assert(information_entropy([]) == 0)
	test = 'abc def abc def'.split()
	assert(information_entropy(test) == 2)
	
def info_gain(A, S):
	"Computes the information gain."
	ig = information_entropy(S)
	for v in set(A):
		Sv = [y for (x, y) in zip(A, S) if x == v]
		ig -= information_entropy(Sv) * (len(Sv) / float(len(S)))
	return ig
	
if __name__=="__main__":
	test_frequencies()
	test_information_entropy()
	print 'tests ok'
