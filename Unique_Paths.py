m, n = 3, 2 
def uniq_path(m,n, i=1, j=1, count=0):
  if i == m and j == n:
    count += 1
  else:
    if i< m:
      count = uniq_path(m,n, i+1, j, count)
    if j < n:
      count = uniq_path(m,n, i, j+1, count)
  return count
print uniq_path(m,n)

