#Joseph Reis
#CS3100, Assignment1

def PythonEx1():
  ordz = ord('z')
  print(ordz)
  
  for ch in range(26):
    print(chr(ordz - ch), end = ' ')
  print('')

if __name__== "__main__":
  PythonEx1()
