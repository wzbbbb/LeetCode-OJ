#A = [3,4,6,9,9]
A = [3,4,6,9,0]
def plus_one(A):
  n = len(A)
  print A
  A.reverse()
  up = 1
  for i in range(n):
    if A[i] + up == 10:
      A[i] , up = 0 , 1
    else:
      A[i] = A[i] + up
      up = 0
  A.reverse()
  return A

print plus_one(A)


