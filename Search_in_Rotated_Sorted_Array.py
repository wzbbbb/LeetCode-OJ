A=[4,7,10,-2,0,2]
t=4
def search(A,t):
  n = len(A)
  if t >= A[0]:
    for i in range(n):
      if t == A[i]: 
        return i
      elif t < A[i]: 
        return -1
      if A[i] < A[i-1]:
        break
  else:
    for i in range(n-1, -1, -1): 
      if t == A[i]: 
        return i
      elif t > A[i]:
        return -1
      if A[i] < A[i-1]:
        break
  return -1
print search(A,t)
