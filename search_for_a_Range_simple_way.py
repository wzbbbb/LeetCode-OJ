A = [5, 7, 7, 8, 8, 8, 10]
target = 8

def search(A, target):
  n = len(A)
  idx_a, idx_b = -1, -1
  for i in range(n):
    if A[i] == target:
      if idx_a == -1: 
        idx_a = i
      else: 
        idx_b = i
  return [idx_a, idx_b]
print search(A, target)


