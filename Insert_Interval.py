A = [ [1,2],[3,5],[6,7],[8,10],[12,16] ]
B = [0,9]
def insert_interval(A, B):
  res = []
  n = len(A) + 1
  A.append(B)
  C = sorted(A, key = lambda x:x[0])
  current_interval = C[0]
  print C
  for i in range(1, n):
    if current_interval[1] > C[i][0] : # merge
      upper_bound = max(C[i][1], current_interval[1])
      current_interval = [current_interval[0],upper_bound]
    else: 
      res.append(current_interval)
      current_interval = C[i]
  res.append(current_interval)
  return res
print  insert_interval(A, B)
