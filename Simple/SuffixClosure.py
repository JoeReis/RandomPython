#Joseph Reis
#CS3100, Assignment1

def suffclosure(s):
  return { s[i:len(s):] for i in range(len(s)+1) }

#test output
#output to a file
def run_suffclosure():
  f = open('SuffixClosure.out','w')
  f.write(str(suffclosure("")))
  f.write(str(suffclosure("a")))
  f.write(str(suffclosure("(((()")))
  f.write(str(suffclosure(";ajsdlkfjalsj d")))
  f.close()

if __name__ == "__main__":
	run_suffclosure()
