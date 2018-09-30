A = [2,1,0,0,1,1,2,0,2,2,0,1,1,1,0]

def sort(A):
  ''' count how many 0, 1 and 2 then, assigin to A
  '''
  r,w,b = 0, 0, 0
  n = len(A)
  for a in A:
    if a == 0: r +=1
    if a == 1: w +=1 
    if a == 2: b +=1
  w += r
  b += w
  A[:r] = [0]* r
  A[r:w] = [1]* (w - r)
  A[w:] = [2]* (b - w)
  # or in this way
  #for i in range(n):
  #  if i < r: 
  #    A[i] = 0
  #  if r <= i< w: 
  #    A[i] = 1
  #  if i >= w: 
  #    A[i] = 2
  return A
print A
print sort(A)
