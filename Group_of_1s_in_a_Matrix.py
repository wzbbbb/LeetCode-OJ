A = [
      [1,1,0,0,1],
      [1,0,0,1,1],
      [1,1,0,1,0],
      [0,0,1,0,0],
    ]
''' once meet '1' find all '1' connected to it, 
    and loop through all items
'''
def find_groups(A):
  res = []
  n = len(A)
  m = len(A[0])
  for i in range(n):
    for j in range(m):
      found = False
      if A[i][j] == 1:
        for r in res:
          if (i,j) in r: 
            found = True
            break
        if not found:
          res.append(walk(A,n,m,i,j,out=[]))
  print res
  return len(res)
def walk(A,n,m,p,q,out):
  if A[p][q] == 1 and (p,q) not in out:
    out.append((p,q))
    if q > 0:
      out = walk(A,n,m,p,q-1,out)
    if q < m - 1:
      out = walk(A,n,m,p,q+1,out)
    if p > 0:
      out = walk(A,n,m,p-1,q,out)
    if p < n - 1:
      out = walk(A,n,m,p+1,q,out)
  return out

print find_groups(A)

