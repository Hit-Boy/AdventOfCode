#!/usr/bin/env python3
import sys, argparse, copy

silent=True
args=""

def log(message, end='\n'):
	global silent
	if not silent:
		sys.stderr.write(str(message)+end)

def loginfo(message, end='\n'):
	sys.stderr.write(str(message)+end)

def get_nth_bit(number,position):
	pass

def get_number_of_bits(number):
	pass

def count_number_of_bits_in_column(inputarray,column):
	numbers = []
	number = maxl = i = 0

	for input in inputarray:
		number = str(input.strip())

		if maxl == 0:
			maxl = len(number)

			if column+1 < maxl:
				maxl = column + 1 

			for i in range(0,maxl):
				t = argparse.Namespace()
				t.count0 = 0
				t.count1 = 0
				numbers.append(t)

		for i in range(0,maxl):
			if number[i] == "0":
				numbers[i].count0 += 1
			else:
				numbers[i].count1 += 1
	return numbers[column]

def return_reduced_array(inputaarray,column,bitvaluetoremovestr):
	result = []
	for input in inputaarray:
		if input[column] != bitvaluetoremovestr:
			result.append(input)
	return result

def solve():
	global args
	numbers = []
	numbers1 = []
	ogr = co2sr = 0
	ogrstr = co2srstr = ""

	maxl = t = i = 0

	for input in args.input.readlines():
		number = str(input.strip())
		if maxl == 0:
			maxl = len(number)
		numbers.append(number)

	numbers1 = numbers
	numbers2 = numbers

	for i in range(0,maxl):

		# getting ogr
		if ogrstr == "":
			t = count_number_of_bits_in_column(numbers1,i)
			if t.count1 >= t.count0:
				numbers1 = return_reduced_array(numbers1,i,"0")
			else:
				numbers1 = return_reduced_array(numbers1,i,"1")

			if len(numbers1) == 1:
				ogrstr = numbers1[0]


		if co2srstr == "":
			t = count_number_of_bits_in_column(numbers2,i)
			if t.count1 >= t.count0:
				numbers2 = return_reduced_array(numbers2,i,"1")
			else:
				numbers2 = return_reduced_array(numbers2,i,"0")


			if len(numbers2) == 1:
				co2srstr = numbers2[0]

	ogr = int(ogrstr, 2)
	co2sr = int(co2srstr, 2)

	loginfo('oxygen generatr rating is: {} ({}), co2 scrubber rating is: {} ({}), oxygen generator rating * co2 scrubbing rating is: {}'.format(ogrstr, ogr, co2srstr, co2sr, ogr * co2sr))
		# getting epsiolo

	#loginfo("Final position is {} horizontal and {} of depth, the horizontal * depth is {}".format(horizontal,depth, horizontal * depth))

def main(argv):
	global silent
	global args
	version="1.0.1"

	parser = argparse.ArgumentParser(description='solve day 3 part 2',
		formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('--input', type=argparse.FileType('r'), default='./input', help='input file to use')
	parser.add_argument('--version', action='version', version='%(prog)s '+version, help='Show program version and exit')
	parser.add_argument('--verbose', default=False, action='store_true', help='Enable all log output. It will be sent to stderr.')

	args = parser.parse_args()

	if args.verbose:
		silent=False

	log(str(args))

	solve()

	args.input.close()

if __name__ == "__main__":
	main(sys.argv)
