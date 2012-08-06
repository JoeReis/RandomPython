def Powerset(s):
  if(s == list()):
    return list(list())
  else:
    e = s[0]
    t = s - e
    q = Powerset(t)
    q.union({x + list(e) for x in t})
    return q
    
    
def run_powerset():
  Powerset([1,2,3])

if __name__ == "__main__":
  run_Powerset()
