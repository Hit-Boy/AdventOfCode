#!/usr/bin/env python3
import sys, argparse

silent=True
args=""

def log(message, end='\n'):
	global silent
	if not silent:
		sys.stderr.write(str(message)+end)

def loginfo(message, end='\n'):
	sys.stderr.write(str(message)+end)

def logof3(array,startindex,end='\n'):
	log("{},{},{} = {} ".format(array[startindex], array[startindex+1], array[startindex+2],sumof3(array,startindex)),end=end)

def sumof3(array,startindex):
	return array[startindex]+array[startindex+1]+array[startindex+2]

def solve():
	global args
	measurements = []
	current = currentp1 = largercount = 0
	elementnumber = 0

	for input in args.input.readlines():
		measurements.append(int(input.strip()))

	max = len(measurements)
	log("There are {} elements in the input file".format(max))

	while True:

		try:
			current = sumof3(measurements, elementnumber)
			currentp1 = sumof3(measurements, elementnumber+1)
		except IndexError as e:
			# reached end of list
			break

		logof3(measurements, elementnumber, end='')

		if (currentp1 > current):
			largercount += 1
			log(" + ({})".format(largercount))
		else:
			log("")


		elementnumber += 1

	loginfo("There are {} measurements that are larger then previous".format(largercount))

def main(argv):
	global silent
	global args
	version="1.0.1"

	parser = argparse.ArgumentParser(description='solve puzzle 2',
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
