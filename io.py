import csv
from utility import is_number

def dict_read_csv(file_path, delimiter=',', skip_lines=[]):
	with open(file_path) as f:
		reader = csv.DictReader(f, delimiter = delimiter)
		
		from collections import defaultdict
		data = defaultdict(list)
		for line in reader:
			if reader.line_num in skip_lines:
				continue
			for (k, v) in line.items():
				data[k].append(float(v) if is_number(v) else v)
	return data
	
def read_csv(file_path, delimiter=',', skip_lines=[]):
	with open(file_path) as f:
		reader = csv.reader(f, delimiter = delimiter)
		
		data = []
		for line in reader:
			if reader.line_num in skip_lines:
				continue
			data.append([float(v) if is_number(v) else v for v in line])
	return data
	
def dict_write_csv(file_path, fieldnames, data, delimiter=','):
    with open(file_path, "w") as f:
    	writer = csv.DictWriter(f, delimiter = delimiter, fieldnames = fieldnames) 
    	writer.writeheader()
    	for i in range(72):
    		dict = {}
    		for k in data.keys():
    			dict[k] = data[k][i]
        	writer.writerow(dict)
        	
def write_csv(file_path, data, delimiter=','):
	with open(file_path, "w") as f:
		writer = csv.writer(f, delimiter = delimiter) 
		writer.writerows(data)