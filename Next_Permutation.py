A=[3,7,2]
#A=[2,3,7,8,6]
''' find out the index where A[i] > A[i-1],
    sort ascending A[i] - A[n], find the least but greater than A[i-1], replace with A[i-1]
    again sort ascending A[i] - A[n] 
'''
def next_perm(A):
  n = len(A)
  if A == sorted(A, reverse=True):
    A.reverse()
    return A
  p = 0
  for i in range(n-1, 0, -1):
    if A[i] > A[i-1]:
      p = i 
      break
  A[p:]=sorted(A[p:])
  for j in range(p,n):
    if A[j] > A[p-1]:
      A[p-1], A[j] = A[j], A[p-1]
      break
  A[p:]=sorted(A[p:])
  return A
print A
print next_perm(A)







