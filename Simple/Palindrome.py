#Joseph Reis
#CS3100, Assignment1

def Palindrome(str):
  print(str + str[::-1])

def run_Palindrome():
  Palindrome("abca13")
  Palindrome("(()(")
  Palindrome("")
  Palindrome("z")

if __name__ == "__main__":
  run_Palindrome()
