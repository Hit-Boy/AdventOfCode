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

	previous = -1
	current = largercount = 0

	for input in args.input.readlines():
		current = int(input.strip())
		log(current, end='')

		if (previous == -1):
			previous = current
			log("")
			continue

		if (current > previous):
			largercount += 1
			log(" + ({})".format(largercount))
		else:
			log("")

		previous = current

	loginfo("There are {} measurements that are larger then previous".format(largercount))

def main(argv):
	global silent
	global args
	version="1.0.1"

	parser = argparse.ArgumentParser(description='solve puzzle 1',
		formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('--input', type=argparse.FileType('r'), default='./input', help='input to use')
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
