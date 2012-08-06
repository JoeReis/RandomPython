#!/usr/bin/env python3
#Joseph Reis
#CS3100, HW #3
from MkDFA import *
from DotDFA import *
from recognizes import *

def run_dfa():
	Q = {'S0', 'S1', 'S2'}
	Sigma = {'0','1'} 
	#Delta = {('S0', '0'): 'S3', ('S0', '1'):'S1', ('S1', '0'): 'S2', ('S1', '1'): 'S3', ('S2', '0'):'S1', ('S2','1'):'S2', ('S3', '0'):'S3', ('S3','1'):'S1'}
	#Delta = {('S0','0'):'S1',('S0','1'):'S2',('S1','0'):'S1',('S1','1'):'S2',('S2','0'):'S3',('S2','1'):'S1',('S3','0'):'S2',('S3','1'):'S3'}
	Delta = {('S0','0'):'S0',('S0','1'):'S1',('S1','0'):'S2',('S1','1'):'S0',('S2','0'):'S1',('S2','1'):'S2'}
	q0 = 'S0'
	F = {'S0'}
	
	print("This DFA accepts all binary numbers divisible by 3. Notice the obvious - all binary numbers divisible by 3 occur every third position after 3 (11 in binary).This means you simply need to make a DFA that initially accepts 11, and accepts every third number from 110000..., such as 110000..., 10010000...., 11110000....")
	
	print("\nStrings that are accepted")
	print("1100",accepts(mk_dfa(Q, Sigma, q0, F, Delta),q0,"1100")) #12 - accept
	print("11",accepts(mk_dfa(Q, Sigma, q0, F, Delta),q0,"11")) #3 - accept
	print("11110",accepts(mk_dfa(Q, Sigma, q0, F, Delta),q0,"11110")) #30 - accept
	print("1111",accepts(mk_dfa(Q, Sigma, q0, F, Delta),q0,"1111")) #15 - accept
	print("10010",accepts(mk_dfa(Q, Sigma, q0, F, Delta),q0,"10010")) #18 - accept
	#print("10010",accepts(mk_dfa(Q, Sigma, q0, F, Delta),q0,"10111010"))#
	
	print("\nStrings that are rejected")
	print("100",accepts(mk_dfa(Q, Sigma, q0, F, Delta),q0,"100")) #4 - reject
	print("101",accepts(mk_dfa(Q, Sigma, q0, F, Delta),q0,"101")) #5 - reject
	print("101",accepts(mk_dfa(Q, Sigma, q0, F, Delta),q0,"101")) #5 - reject
	print("111",accepts(mk_dfa(Q, Sigma, q0, F, Delta),q0,"111")) #7 - reject
	print("1010",accepts(mk_dfa(Q, Sigma, q0, F, Delta),q0,"1010")) #10 - reject
	
	
	dot_dfa(mk_dfa(Q, Sigma, q0, F, Delta),'notes5_qn3_DFA.dot')

if __name__ == "__main__":
	run_dfa()