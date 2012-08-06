#!/usr/bin/env python3
#Joseph Reis, CS3100
# Contents of file DotDFA.py

def homos(S,f):
	"""String homomorphism wrt lambda f homos("abcd",hm) --> 'bcde' where hm = lambda x: chr( (ord(x)+1) % 256 )"""
	return "".join(map(f,S))
def dotsan_map(x):
	"""String homomorphism that converts characters in x {"{", " ", "'", "}" } to the empty string, and converts "," to "_"."""
	if x in { "{", " ", "'", "}" }:
		return ""
	elif x == ",":
		return "_"
	else:
		return x
def dot_san_str(S):
	"""Homomorphically maps strings using the homos method, and makes dot like strings which are in set of states notation."""
	return homos(S, dotsan_map)
def prDotHeader(fl):
	"""Print header of dot file with proper font and frame size formatting"""
	print (r'digraph G {', file=fl)
	print (r'/* Defaults */', file=fl)
	print (r' fontsize = 12;', file=fl)
	print (r' ratio = compress; ', file=fl)
	print (r' rankdir=LR; ', file=fl)
	print (r'/* Bounding box */', file=fl)
	print (r' size = "4,4";', file=fl)
def prNonFinalNodeName(fl, q):
	"""Prints the non-final state node's name by calling dot_san_str method on a set and drawing a circle to the dot file indicating the final state."""
	print (dot_san_str(q), r'[shape=circle, peripheries=1];', file=fl)
def prFinalNodeName(fl, q):
	"""Prints the final state (accept state) node's name. Draws a circle to the dot file indicating the final state"""
	# Could write like print (q, r'[shape=circle, peripheries=2];', file=fl)
	# But am documenting use of trailing comma to suppress \n . In Python3 we supply end = ''
	print(dot_san_str(q), file=fl, end='') # end with no CR
	print(r' [shape=circle, peripheries=2];', file=fl) # end with a CR
def prOrientation(fl):
	"""Orients the dot file layout. Defaults to landscape orientation."""
	print(r'/* Orientation */', file=fl)
	print(r'orientation = landscape;', file=fl)
def prEdges_w_bh(fl, D):
	"""Given a set Delta, this method homomorphically maps elements from Delta to the file, and produces edges for the dot file. Also prints black hole suppression."""
	print(r'/* The graph itself */', file=fl)
	print(r'"" -> ', dot_san_str(D["q0"]), ";", file=fl)
	for QcQ in D["Delta"].items():
		print(dot_san_str(QcQ[0][0]), r' -> ',
		dot_san_str(QcQ[1]), r'[label="', dot_san_str(QcQ[0][1]), r'"];', file=fl)
def prEdges(fl, D):
	"""Given a set Delta, this method homomorphically maps elements from Delta to the file. Includes provision for black hole state."""
	print(r'/* The graph itself */', file=fl)
	print(r'"" -> ', dot_san_str(D["q0"]), ";", file=fl)
	for QcQ in D["Delta"].items():
		if (((QcQ[0][0]) != "BH") & (QcQ[1] != "BH")):
			print(dot_san_str(QcQ[0][0]), r' -> ',
			dot_san_str(QcQ[1]), r'[label="', dot_san_str(QcQ[0][1]), r'"];', file=fl)
def prClosing(fl):
	"""Prints the final instructions and messages after the code has executed"""
	print(r'/* Unix command: dot -Tps exdfa.dot >! exdfa.ps */', file=fl)
	print(r"/* For further details, see the `dot' manual */", file=fl)
	print(r"}", file=fl)
def prNodeDefs_w_bh(fl, D):
	"""Prints the state names and language for a specific node. Includes provision for black hole state."""
	print(r'/* Node definitions */', file=fl)
	print(r' "" [shape=plaintext];', file=fl) # Start state arrow is from "" to I
	# All non-accepts are single circles
	for q in D["Q"] - D["F"]:
		prNonFinalNodeName(fl, q)
	for q in D["F"]:
		prFinalNodeName(fl, q)
def prNodeDefs(fl, D):
	"""Prints all node paths and arrows. Includes provision for black hole state."""
	print(r'/* Node definitions */', file=fl)
	print(r' "" [shape=plaintext];', file=fl) # Start state arrow is from "" to I
	# All non-accepts are single circles
	for q in D["Q"] - D["F"]:
		if (q != "BH"):
			prNonFinalNodeName(fl, q)
	for q in D["F"]:
		prFinalNodeName(fl, q)
def dot_dfa(D, fname):
	"""Generate a dot file with the automaton in it. Run the dot file through dot and generate a ps file."""
	fl = open(fname, 'w')
	#fl = open(DotDFA.dot,'w')
	#-- digraph decl
	prDotHeader(fl)
	#-- node names and how to draw them
	prNodeDefs(fl, D)
	#-- orientation - now landscape
	prOrientation(fl)
	#-- edges
	prEdges(fl, D)
	#-- closing
	prClosing(fl)
def run_Dot():
	"""Method run when DotDFA is executed from the console. Produces the help instruction and a DotDFA.dot file"""
	print(help(homos))
	print(help(dotsan_map))
	print(help(dot_san_str))
	print(help(prDotHeader))
	print(help(prNonFinalNodeName))
	print(help(prFinalNodeName))
	print(help(prOrientation))
	print(help(prEdges_w_bh))
	print(help(prEdges))
	print(help(prClosing))
	print(help(prNodeDefs_w_bh))
	print(help(prNodeDefs))
	print(help(dot_dfa))
	print(help(run_Dot))
	Q = {'S0','S1'}
	Sigma = {'a','b'}
	Delta = {('S0', 'a'): 'S0', ('S1', 'a'): 'S0', ('S1', 'b'): 'S1', ('S0', 'b'): 'S1'}
	q0 = 'S0'
	F = {'S1'}
	dot_dfa({"Q":Q, "Sigma":Sigma, "Delta":Delta, "q0":q0, "F":F}, 'DotDFA.dot')
	#Q = {'S0','S1', 'S2','S3','S4'}
	#Sigma = {'0','1'}
	#Delta = {('S0', '0'): 'S1', ('S0', '1'): 'S0', ('S1', '0'): 'S0', ('S1', '1'): 'S2', ('S2','0'): 'S3', ('S2','1'): 'S0', ('S3','0'):'S1', ('S3','1'):'S4', ('S4','0'):'S1',('S4','1'):'S0'}
	#q0 = 'S0'
	#F = {'S4'}
	#dot_dfa({"Q":Q, "Sigma":Sigma, "Delta":Delta, "q0":q0, "F":F}, 'Dot0101.dot')
	
if __name__ == "__main__":
	run_Dot()