m, n = 4, 3 
A = [
  [0,0,0],
  [0,1,0],
  [0,0,0],
  [0,0,0]
]
def uniq_path(A, m,n, i=0, j=0, count=0):
  if i == m-1 and j == n-1:
    count += 1
  else:
    if i< m -1: 
     if A[i+1][j] != 1:
        count = uniq_path(A, m,n, i+1, j, count)
    if j < n-1:
      if A[i][j+1] != 1:
        count = uniq_path(A, m,n, i, j+1, count)
  return count
print uniq_path(A, m,n)

