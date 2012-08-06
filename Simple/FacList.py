#Joseph Reis
#CS3100, Assignment1

def FacList(N):
    
    if N <= 1:
      return 1
    else:
      return N * FacList(N-1)

#output to a file
def run_FacList():
	f = open('FacList.out','w')
	f.write(str([FacList(i) for i in range(2 + 1)]))
	f.write(str([FacList(i) for i in range(1 + 1)]))
	f.write(str([FacList(i) for i in range(10 + 1)]))
	f.write(str([FacList(i) for i in range(50 + 1)]))
	f.close()


if __name__ == "__main__":
  run_FacList()
