#A = [2,3,0,2,1,0,1,2,2,0,2,0]
A = [2,1,2,2,2,0]
def water(A):
  ''' calculate from top to bottom 
      find water in each level
  '''
  m = max(A) 
  n = len(A)
  res = 0
  while m > 0:
    level =[]
    for i in range(n): 
      if A[i] >= m :
        level.append(i)
    k = len(level)
    for l in range(1, k):
      res += level[l] - level[l-1] -1
    m -=1
  return res
print water(A)
