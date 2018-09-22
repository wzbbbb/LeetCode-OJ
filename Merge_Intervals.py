A=[[1,3],[2,6],[10,19],[5,8]]
def merge(A):
  B = sorted(A, key = lambda x:x[0])
  n = len(A)
  res = []
  current_interval = B[0]
  for i in range(1, n):
    if B[i][0] <= current_interval[1]: # overlapping
      if B[i][1] > current_interval[1]:
        current_interval[1] = B[i][1]
    else:
      res.append(current_interval)
      current_interval = B[i]
  res.append(current_interval)
  return res
print merge(A)

