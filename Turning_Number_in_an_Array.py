# O(n)
A = [-3,-1, 0, 1,  2,  3,  4,  5,  10,  9,  8,  7,  6]
def turning_number(A):
  n = len(A)
  for i in range(1,n): 
    if A[i] < A[i -1]:
      return i -1
print turning_number(A)

# O(log(n)) binary search ! :)
def turn(A):
  n = len(A)
  i = n//2
  while True:
    if  A[i-1] < A[i] > A[i+1]:
      return i
    elif A[i] > A[i-1] :
      i = (i + n -1) // 2
    elif A[i] < A[i-1] :
      i = i//2
print turn(A)




