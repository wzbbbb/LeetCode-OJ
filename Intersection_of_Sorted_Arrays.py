A = [1, 4, 7, 10, 13]
B = [1, 3, 5, 7, 9, 13]

''' Moving and comparing one by one, since it is sorted
    O(m+n)
'''
def intersection(A,B):
  i, j = 0, 0
  n = len(A)
  m = len(B)
  res = []
  while i < n and j < m:
    if A[i] == B[j]:
      res.append(A[i])
      i += 1
      j += 1
    elif A[i] > B[j]:
      j += 1
    else:
      i += 1
  return res
print  intersection(A,B)

''' can also use binary search A[i] in B 
'''
# does not work
def intersection_bin(A,B):
  i, j = 0, 0 
  n = len(A)
  m = len(B)
  res = []
  while i < n and j < m:
    if A[i] == B[j]:
      res.append(A[i])
      i += 1
      j += 1
    elif A[i] < B[j] < A[i+1]:
      i += 1
      j += 1
    elif A[i] > B[j]:
      j = (j + m - 1)//2
    else:
      j = j //2
  return res

print  intersection_bin(A,B)
