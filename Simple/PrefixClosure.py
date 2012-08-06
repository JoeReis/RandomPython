#Joseph Reis
#CS3100, Assignment1

def prefixclosure(s):
  return { s[:i] for i in range(len(s) + 1) }

#test output
#write to a file
def run_prefixclosure():
	f = open('PrefixClosure.out','w')
	#f.write(str(prefixclosure("")))
	#f.write(str(prefixclosure("a")))
	#f.write(str(prefixclosure("(((())")))
	f.write(str(prefixclosure(";ajsdlkfjalsj dd")))
	#f.close()

if __name__ == "__main__":
	run_prefixclosure()
