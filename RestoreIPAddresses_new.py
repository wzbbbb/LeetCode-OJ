#A = '25525511135'
A = '223456'
def restore_address(A):
  n = len(A)
  res = []
  for i in range(1,4): 
    a = A[:i]
    if int(a) > 255:
      continue
    for j in range(1,4):
      b = A[i:i+j]
      if int(b) > 255:
        continue
      for k in range(1,4):
        c = A[i+j:i+j+k]
        if int(c) > 255:
          continue
        for m in range(1,4):
          if i+j+k+m > n:
            break
          d = A[i+j+k:i+j+k+m]
          if int(d) > 255 or i+j+k+m < n :
            continue
          if i+j+k+m  == n :
            res.append(a + '.' + b + '.' + c + '.' + d)
  return res
print  A 
print restore_address(A)
