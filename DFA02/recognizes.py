#!/usr/bin/env python3
#Joseph Reis
from MkDFA import *
from math import *

def recognizes(D,N):
	for i in range(0,int(pow(2,N+1) - 2)):
		if(accepts(D, D["q0"],nthnumeric(i))):
			print (nthnumeric(i))
	
def step_dfa(D,q,c):
	"""Run DFA D from state q on character c. Return the next state."""
	assert(c in D["Sigma"])
	assert(q in D["Q"])
	return D["Delta"][(q,c)]
	
def run_dfa(D,q,s):
	"""Run DFA D from state q on string S. Return the next state."""
	return q if s=="" else run_dfa(D,step_dfa(D,q,s[0]),s[1:])
	
def accepts(D,q,s):
	"""Checks for DFA acceptance"""
	return run_dfa(D,q,s) in D["F"]
	
def nthnumeric(N):
	"""Assume that Sigma is {a,b}. Produce the Nth string in numeric order, where N >= 0. Idea : Given N, get b = floor(log_2(N+1)) - need that many places; what to fill in the places is the binary code for N - (2^b - 1) with 0 as a and 1 as b."""
	if(N==0):
		return ''
	else:
		width = floor(log(N+1, 2))
		tofill = int(N - pow(2, width) + 1)
		relevant_binstr = bin(tofill)[2::] # strip the 0b leading string
		len_to_makeup = width - len(relevant_binstr)
		return "0"*len_to_makeup + homos(relevant_binstr, lambda x: '1' if x=='1' else '0')
		
def homos(S,f):
	return "".join(map(f,S))
	
def run_recognizes():
	Q = {'S0','S1', 'S2','S3','S4'}
	Sigma = {'0','1'}
	Delta = {('S0', '0'): 'S1', ('S0', '1'): 'S0', ('S1', '0'): 'S1', ('S1', '1'): 'S2', ('S2','0'): 'S3', ('S2','1'): 'S0', ('S3','0'):'S1', ('S3','1'):'S4', ('S4','0'):'S1',('S4','1'):'S0'}
	q0 = 'S0'
	F = {'S4'}
	N = 5

	print(recognizes(mk_dfa(Q, Sigma, q0, F, Delta), N))
	
if __name__ == "__main__":
	run_recognizes()