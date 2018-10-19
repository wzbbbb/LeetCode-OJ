A = [1, 2, 3, 4, 5] 
B = [3, 2, 4, 5, 1]
''' if the pop sequence is different, 
    it means that need to push the next one before push again
'''
def push_pop(A,B):
  stack = []
  res = []
  n = len(A)
  i, j = 0, 0
  while i < n and j < n:
    while i < n: 
      if A[i] == B[j]:
        stack.append(A[i])
        i += 1
        break
      stack.append(A[i])
      i += 1
    while stack:
      if stack[-1] == B[j]:
        res.append(stack.pop())
        j += 1
      else: 
        break
  return res == B
print push_pop(A,B)
