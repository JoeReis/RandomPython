def Powerset(s):
  s = list(s)
  if s == []:
    return [[]]
  else:
    e = [s[0]]
    t = s[::1]
    t.remove(e[0])
    q = Powerset(t)
    #return q + [x + e for x in q]
    return Powerset(t) + [x + e for x in q]
    
    
def run_Powerset():
  print (Powerset([1,2,3]))
  print (Powerset({1,2,3}))

if __name__ == "__main__":
  run_Powerset()
