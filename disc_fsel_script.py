import io
from discretize import *
from collections import defaultdict

MAX_GENES = 24
CLASS_COLUMN_NAME = 'gene'

def select_features(data, classes, num_of_feature):
	# compute the best threshold and the corresponding info-gain for each gene"
	features = []
	for (gene, values) in data.items():
		h_ig, h_threshold = highest_infogain_threshold(values, classes)
		features.append((gene, h_ig, h_threshold))
	
	# choose a small subset of the best genes when sorted by info-gain
	features.sort(key=lambda t: t[1], reverse=True)
	
	del features[num_of_feature:]
	return features

def main():
	# load data from file
	data = io.dict_read_csv('data/leukemia.tab', '\t', [2, 3])
	# divide data in classes, genes data
	classes = list(data[CLASS_COLUMN_NAME])
	del data[CLASS_COLUMN_NAME]

	# feature selection
	features = select_features(data, classes, MAX_GENES)

	# discretize each gene values according to its best threshold
	discretized_data = defaultdict(list)
	for (gene, _, threshold) in features:
		discretized_data[gene] = binary_discretization(data[gene], threshold)
	
	# write to a results CSV file
	discretized_data[CLASS_COLUMN_NAME] = classes
	fieldnames = discretized_data.keys()
	if CLASS_COLUMN_NAME in fieldnames:
		del fieldnames[fieldnames.index(CLASS_COLUMN_NAME)]
		fieldnames.append(CLASS_COLUMN_NAME)
		
	io.dict_write_csv('data/disc_fselected.csv', fieldnames, discretized_data)
	
if __name__=="__main__":
    main()
	
	