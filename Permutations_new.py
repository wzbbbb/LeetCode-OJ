A = [1,2,3,4]
''' form the base items [1],[2],[3]
    add all items one by one, each time create a new list
    then, check if all the lists has the full length, complete!
'''
def permu(A):
  res = []
  for a in A:
    res.append([a])
  Running = True
  while Running:
    tmp2 = []
    for r in res:
      for a in A:
        tmp1 = r[:]
        #print tmp1, tmp2
        if a not in r:
          tmp1.append(a)
          tmp2.append(tmp1)
    res = tmp2[:]
    Running = False
    for r in res:
      if len(r) < len(A):
        Running = True
        break
  return res

print permu(A)
