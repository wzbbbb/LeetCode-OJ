A = [ ['A', 'B', 'C', 'E' ],
      ['S', 'F', 'C', 'S' ],
      ['A', 'D', 'E', 'E' ]
    ]

s ='SFDECCESC'
def find_path(A, s):
  n = len(A)
  m = len(A[0])
  for i in range(n): 
    for j in range(m): 
      if walk(A, s, i, j, n, m, res=False, k=0, ss='', coor=[]): 
        return True
  return False
     

def walk(A, s, i, j, n, m, res, k, ss, coor): 
  if A[i][j] == s[k] and (i,j) not in coor:
    ss += A[i][j]
    coor.append((i,j))
    k +=1
    if ss == s:
      return True
    if i < n-1:
      res = walk(A, s, i+1, j, n, m,  res, k, ss, coor)
    if i > 0:
      res = walk(A, s, i-1, j, n, m, res, k, ss, coor)
    if j < m-1:
      res = walk(A, s, i, j+1, n, m, res, k, ss, coor)
    if j >0:
      res = walk(A, s, i, j-1, n, m, res, k, ss, coor)
  return res
print find_path(A,s)





