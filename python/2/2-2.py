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


def solve():
	global args
	measurements = []
	horizontal = depth = aim = 0
	command = ""
	down = "down"
	forward = "forward"
	up = "up"

	arg1 = 0

	for input in args.input.readlines():
		(command, arg1) = input.split(" ",2)
		command = command.strip()
		arg1 = int(arg1)
		log("command: {}, argument: {}".format(command,arg1))
		
		if command == down:
			aim += arg1
			continue

		if command == up:
			aim -= arg1
			continue

		if command == forward:
			horizontal += arg1
			depth += aim * arg1

	loginfo("Final position is {} horizontal and {} of depth, the horizontal * depth is {}".format(horizontal,depth, horizontal * depth))

def main(argv):
	global silent
	global args
	version="1.0.1"

	parser = argparse.ArgumentParser(description='solve puzzle 2 part 2',
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
