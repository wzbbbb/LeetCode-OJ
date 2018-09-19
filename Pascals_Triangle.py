''' B[i] = A[i-1] + A[i]        '''
n = 5
def pascal_triangle(n):
  A = [1,1]
  if n < 1 : return None
  if n == 1 : return [1]
  if n == 2 : return [1,1]
  for i in range(2, n+1):
    B = [0] * (i+1)
    for j in range(i+1):
      if j == 0 or j == i: 
        B[j] = 1
        continue
      B[j] = A[j-1] + A[j]
    print B
    A = B[:]
  return B
print  pascal_triangle(n)
