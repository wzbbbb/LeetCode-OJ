n = 10 
def spiral(n):
  a = 0
  A = [[0]*n for i in range(n) ]
  for k in range(n - 1):
    for i in range(k, n-k):
      a += 1
      A[k][i] = a
    for j in range(k+1, n-k):
      a += 1
      A[j][n-k-1] = a
    for p in range(n-k-2, k-1, -1):
      if n - k - 1 == k: break
      a += 1
      A[n-k-1][p] = a
    for q in range(n-k-2, k, -1):
      if n-k-1 == k: break
      a += 1
      A[q][k] = a
  return A
A = spiral(n)
for a in A:
  print a

#print spiral(n)

