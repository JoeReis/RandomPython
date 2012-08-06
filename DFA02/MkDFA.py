#!/usr/bin/env python3
#Joseph Reis, CS3100
from DotDFA import *

def mk_dfa(Q, Sigma, q0,F, Delta):
	#"""Make a DFA with the given traits. Delta is supplied as a hash-map (dict).
	#"""
	# Do all the checks listed in boldface fonts, above, using Python asserts.
	#
	# If all OK, return DFA as a dict
	#Q is a nonempty set of String
	assert Q
	#Sigma is a set of non-empty single-character strings (alphabet)
	assert Sigma
	for s in Sigma:
		assert(len(s) != None)
	#q0 is a state belonging to Q
	assert q0 in Q
	# F is a possibly non-empty set of states, and is also a subset of and
	#is also a subset of Q
	for i in F:
		assert i in Q
	#Delta is a total function represented as a hash-table, mapping a pair (q; c) (where
	#q in Q and c in Sigma) to a new state q1 where q1 is also in Q.	
	for q in Delta.keys():
		assert q[0] in Q
		assert q[1] in Sigma
	for c in Delta.values():
		assert c in Q
	return({"Q":Q, "Sigma":Sigma, "Delta":Delta, "q0":q0, "F":F})
def run_mkDFA():
	Q1 = {'S0','S1'}
	Sigma1 = {'a','b'}
	Delta1 = {('S0', 'a'): 'S0', ('S1', 'a'): 'S0', ('S1', 'b'): 'S1', ('S0', 'b'): 'S1'}
	q01 = 'S0'
	F1 = {'S1'}
	print(mk_dfa(Q1, Sigma1, q01, F1, Delta1))
	dot_dfa(mk_dfa(Q1, Sigma1, q01, F1, Delta1),'DotDFA.dot')
	
if __name__ == "__main__":
	run_mkDFA()