#A = [5, 7, 7, 8, 8, 10]
A = [5]
t = 1
def search(A,t):
  n = len(A)
  start, end = -1, -1
  for i in range(n):
    if A[i] == t : 
      if start == -1:
        start = i
      else:
        end = i
  if start > end: 
    end = start
  return [start, end]
print search(A,t)
