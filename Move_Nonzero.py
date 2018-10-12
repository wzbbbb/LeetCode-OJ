A = [0,2,4,0,7, 5, 0,9,3]
def move(A):
  n = len(A)
  p, q = 0, n - 1
  while p <= q:
    if A[p] != 0:
      p += 1
    if A[q] == 0:
      q -= 1
    if p < q and A[p] == 0 and A[q] != 0:
      A[p] = A[q]
      p += 1
      q -= 1
  print A
  return p
print move(A)
