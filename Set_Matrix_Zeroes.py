A =[
    [1,   3,  5,  0],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
   ]
def zeros(A):
  m=len(A)
  n=len(A[0])
  res = []
  for i in range(m):
    for j in range(n):
      if A[i][j] == 0:
        res.append((i,j))
  for r in res:
    for i in range(n):
      A[r[0]][i] = 0
    for j in range(m):
      A[j][r[1]] = 0
  print  A

print  A
print zeros(A)
