k = 8
''' tmp[i] = res[i] + res[i-1] 
'''
def pascalII(k):
  if k == 1: return [1]
  if k == 2: return [1,1]
  tmp = [1,1]
  for i in range(3,k+1): 
    res = [1]
    n = len(tmp)
    for i in range(1,n):
      res.append(tmp[i] + tmp[i-1])
    res.append(1)
    tmp = res[:]
  return res
print pascalII(k)



