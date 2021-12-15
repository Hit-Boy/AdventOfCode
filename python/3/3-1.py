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

def get_nth_bit(number,position):
	pass

def get_number_of_bits(number):
	pass

def solve():
	global args
	numbers = []
	measures = []
	epsilon = gamma = 0
	epsilonstr = gammastr = ""

	maxl = size = i = 0

	for input in args.input.readlines():
		number = str(input.strip())

		if maxl == 0:
			maxl = len(number)

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

		log("number: {}".format(number))

	for i in range(0,maxl):
		# getting gamma
		if numbers[i].count1 > numbers[i].count0:
			gammastr = gammastr + '1'
			epsilonstr = epsilonstr + '0'
		else:
			gammastr = gammastr + '0'
			epsilonstr = epsilonstr + '1'

	gamma = int(gammastr, 2)
	epsilon = int(epsilonstr, 2)

	loginfo('gamma binary is: {} ({}), epsilon binary is: {} ({}), gamma * epsilon is: {}'.format(gammastr, gamma, epsilonstr, epsilon, gamma * epsilon))
		# getting epsiolo

	#loginfo("Final position is {} horizontal and {} of depth, the horizontal * depth is {}".format(horizontal,depth, horizontal * depth))

def main(argv):
	global silent
	global args
	version="1.0.1"

	parser = argparse.ArgumentParser(description='solve day 3 part 1',
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
