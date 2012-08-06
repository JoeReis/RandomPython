#!/usr/bin/env python3
#Joseph Reis
#CS3100, HW #3
from MkDFA import *
from DotDFA import *
from recognizes import *

def run_dfa():
	#Q = {'S0', 'S1'}
	Q = {'S0','S1','S2','S3','S4','S5','S6'}
	Sigma = {'0','1'} 
	
	#Delta = {('S0', '0'): 'S3', ('S0', '1'):'S1', ('S1', '0'): 'S2', ('S1', '1'): 'S3', ('S2', '0'):'S1', ('S2','1'):'S2', ('S3', '0'):'S3', ('S3','1'):'S1'}
	#Delta = {('S0','0'):'S1',('S0','1'):'S2',('S1','0'):'S1',('S1','1'):'S2',('S2','0'):'S3',('S2','1'):'S1',('S3','0'):'S2',('S3','1'):'S3'}
	#Delta = {('S0','0'):'S0',('S0','1'):'S1',('S1','0'):'S1',('S1','1'):'S1'}
	Delta = {('S0','0'):'S0',('S0','1'):'S1',('S1','0'):'S3',('S1','1'):'S2',('S2','0'):'S4',('S2','1'):'S2',('S3','0'):'S3',('S3','1'):'S5',('S4','0'):'S4',('S4','1'):'S6',('S5','0'):'S3',('S5','1'):'S6',('S6','0'):'S4',('S6','1'):'S6'}
	q0 = 'S0'
	F = {'S1','S2','S3','S4','S5','S6'}
	#F = {'S1'}
	
	print("This DFA concatenates the DFAs in Figure 1 and Figure 5 in Notes 5. Figure 1 accepts all strings ending in one. Figure 2 accepts all strings starting and ending with the same character. When these are concatenated, the new DFA concatenates these two DFAs.")
	print(mk_dfa(Q, Sigma, q0, F, Delta))
	print("\nFive strings accepted in the language:")
	print("1001",accepts(mk_dfa(Q, Sigma, q0, F, Delta),q0,"1010"))#true
	print("0001", accepts(mk_dfa(Q, Sigma, q0, F, Delta),q0,"0001"))#true
	print("0101",accepts(mk_dfa(Q, Sigma, q0, F, Delta),q0,"0101"))#true
	print("101",accepts(mk_dfa(Q, Sigma, q0, F, Delta),q0,"100"))#true
	print("11111",accepts(mk_dfa(Q, Sigma, q0, F, Delta),q0,"100"))#true
	print("\nFive strings not accepted, not in the language")
	#print("2222",accepts(mk_dfa(Q, Sigma, q0, F, Delta),q0,"2222"))#false
	print("00000",accepts(mk_dfa(Q, Sigma, q0, F, Delta),q0,"00000"))#false
	print("0000",accepts(mk_dfa(Q, Sigma, q0, F, Delta),q0,"0000"))#false
	print("000",accepts(mk_dfa(Q, Sigma, q0, F, Delta),q0,"000"))#false
	print("00",accepts(mk_dfa(Q, Sigma, q0, F, Delta),q0,"00"))#false
	print("0",accepts(mk_dfa(Q, Sigma, q0, F, Delta),q0,"0"))#false
	
	#dot_dfa(mk_dfa(Q, Sigma, q0, F, Delta),'notes5_qn5_DFA.dot')

if __name__ == "__main__":
	run_dfa()