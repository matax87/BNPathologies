import io
from split import train_test_prop_split

def main():
	# load data from file
	data = io.read_csv('data/disc_fselected.csv')

	# split data proportionally on the last column into training, test sets
	train, test = train_test_prop_split(data[1:], 0.2, -1)
	
	# add headers
	train.insert(0, data[0])
	test.insert(0, data[0])

	# write training, test sets to CSV files		
	io.write_csv('data/training.csv', train)
	io.write_csv('data/test.csv', test)
	
if __name__=="__main__":
    main()