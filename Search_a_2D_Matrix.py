A =[
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
   ]
t =11
def search(A,t):
  n = len(A)
  row = -1
  for i in range(n):
    if t in range(A[i][0], A[i][-1] +1):
      row = i
  if row == -1: 
    return False
  for k in A[row]: 
    if t == k : return True
    if k > t: return False
  return False
print search(A,t)
