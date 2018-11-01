a = 8763531
''' start from the back, find the first digit that is not ascending 
    then find the first digit greater than it, attach to the string
    then sort ascending and attach the rest
''' 
def next_num(a):
  b = str(a)[::-1]
  n = len(b)
  res = [int(b[0])]
  j = None
  for i in range(1,n):
    res.append(int(b[i]))
    if int(b[i]) < int(b[i-1]): 
      j = i
      break
  if j == None: 
    return a
  res.sort()
  for r in res:
    if r > int(b[j]): 
      res.remove(r)
      out = str(r)
      break
  for r in res: 
    out = out + str(r)

  out = b[:j:-1] + out
  return out
print a
print next_num(a)

  

