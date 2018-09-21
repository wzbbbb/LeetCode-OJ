''' 
[0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8]
0,1,3,2 -> 2+4, 3+4,1+4,0+4, 4 -> 2^2 ...
'''
n=5
def gray(n):
  if n == 1: return [0,1]
  A = [0,1]
  for i in range(2,n+1):
    tmp = A[:]
    m = len(A)
    for j in range(m-1,-1, -1):
      tmp.append(2**(i-1) + A[j])
    A = tmp[:]
  return A
print gray(n)


