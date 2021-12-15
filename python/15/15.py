#!/usr/bin/env python3
import sys, argparse, copy
import networkx as nx
from networkx.algorithms.shortest_paths.weighted import single_source_dijkstra
import matplotlib.pyplot as plt

silent=True
args=""

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   BACK = '\033[A'

def log(message, end='\n'):
	global silent
	if not silent:
		sys.stderr.write(str(message)+end)

def loginfo(message, end='\n'):
	sys.stderr.write(str(message)+end)

def print_riskarray(riskarray):
	r = c = 0
	for r in range(0,riskarray.maxr):
		for c in range(0,riskarray.maxc):
			if riskarray.row[r].col[c].visited == False:
				print("{}".format(riskarray.row[r].col[c].risk),end='')
			else:
				print(color.BOLD + "{}".format(riskarray.row[r].col[c].risk) + color.END,end='')
		print()
	print()

def load_data():
	global args

	r = c = 0
	riskarray = argparse.Namespace()
	riskarray.row = []
	riskarray.graph = []
	riskarray.maxc = -1
	riskarray.maxr = -1

	r = 0
	for input in args.input.readlines():
		line = input.strip()
		riskarray.row.append(line)

		if riskarray.maxc == -1 or riskarray.maxc < len(line):
			riskarray.maxc = len(line)

		r += 1

	riskarray.maxr = r

	return riskarray

def enlarge_data(riskarray, size: int = 5):
	#n = copy.deepcopy(riskarray)
	n = argparse.Namespace()
	n.row = []
	n.graph = []
	n.maxc = riskarray.maxc * size
	n.maxr = riskarray.maxr * size


	for ir in range(size):
		for r in range(riskarray.maxr):
			string = ""
			for ic in range(size):
				for c in range(riskarray.maxc):
					candidate = (int(riskarray.row[r][c])+ic+ir-1) % 9 + 1
					string+= str(candidate)
			n.row.append(string)
			log(string)

	return n

def load_graph(riskarray):
	global args

	G = nx.DiGraph()
	r = c = 0
	riskarray.graph = G

	for r in range(0,riskarray.maxr):
		for c in range(0,riskarray.maxc):
			#down
			if r+1 < riskarray.maxr and r+1 >= 0:
				log("Adding edge from {} to {} with weight {}".format(str(r)+','+str(c),str(r+1)+','+str(c),int(riskarray.row[r+1][c])))
				riskarray.graph.add_edge(str(r)+','+str(c),str(r+1)+','+str(c),weight=int(riskarray.row[r+1][c]))
			#up
			if r-1 < riskarray.maxr and r-1 >= 0:
				log("Adding edge from {} to {} with weight {}".format(str(r)+','+str(c),str(r-1)+','+str(c),int(riskarray.row[r-1][c])))
				riskarray.graph.add_edge(str(r)+','+str(c),str(r-1)+','+str(c),weight=int(riskarray.row[r-1][c]))
			#right
			if c+1 < riskarray.maxc and c+1 >= 0:
				log("Adding edge from {} to {} with weight {}".format(str(r)+','+str(c),str(r)+','+str(c+1),int(riskarray.row[r][c+1])))
				riskarray.graph.add_edge(str(r)+','+str(c),str(r)+','+str(c+1),weight=int(riskarray.row[r][c+1]))
			#left
			if c-1 < riskarray.maxc and c-1 >= 0:
				log("Adding edge from {} to {} with weight {}".format(str(r)+','+str(c),str(r)+','+str(c-1),int(riskarray.row[r][c-1])))
				riskarray.graph.add_edge(str(r)+','+str(c),str(r)+','+str(c-1),weight=int(riskarray.row[r][c-1]))

	return riskarray

def solve1(riskarray):
	global args
	risk = -1

	riskarray = load_graph(riskarray)
	risk, path = nx.single_source_dijkstra(riskarray.graph,'0,0',str(riskarray.maxr-1)+','+str(riskarray.maxc-1),weight="weight")
	#risk = nx.shortest_path_length(riskarray.graph, '0,0', str(riskarray.maxr-1)+','+str(riskarray.maxc-1),weight="weight")

	# i = 0
	# for item in path:
	# 	r,c = item.split(',')
	# 	r = int(r)
	# 	c = int(c)

	# 	if r == c == 0:
	# 		continue
		
	# 	i += int(riskarray.row[r][c])
	# 	log("adding {} {} - {} ({})".format(r,c,int(riskarray.row[r][c]),i))


	log("lowest risk - {}, path is: {}".format(risk,path))

	loginfo("The lowest risk is {}".format(risk))

def solve2(riskarray):
	global args
	risk = -1

	riskarrayn = enlarge_data(riskarray)

	riskarray = load_graph(riskarrayn)

	risk, path = nx.single_source_dijkstra(riskarrayn.graph,'0,0',str(riskarrayn.maxr-1)+','+str(riskarrayn.maxc-1),weight="weight")

	log("lowest risk - {}, path is: {}".format(risk,path))

	loginfo("The lowest risk is {}".format(risk))

def main(argv):
	global silent
	global args
	version="1.0.1"

	parser = argparse.ArgumentParser(description='solve day 3 both parts',
		formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('--input', type=argparse.FileType('r'), default='./input', help='input file to use')
	parser.add_argument('--version', action='version', version='%(prog)s '+version, help='Show program version and exit')
	parser.add_argument('--verbose', default=False, action='store_true', help='Enable all log output. It will be sent to stderr.')

	args = parser.parse_args()

	if args.verbose:
		silent=False

	log(str(args))

	riskarray = load_data()

	solve1(riskarray)
	solve2(riskarray)

	args.input.close()

if __name__ == "__main__":
	main(sys.argv)
