A=[100, 2, 7, 11, 15, 10]
t=111
def twosum(A,t):
  n = len(A)
  dic=dict()
  for i in range(n): 
    dic[A[i]] = i
  A.sort()
  for i in range(n - 1):
    for j in range(i + 1, n):
      if A[i] + A[j] == t:
        ind1 = min(dic[A[i]], dic[A[j]])
        ind2 = max(dic[A[i]], dic[A[j]])
        return   ind1 + 1, ind2 + 1
      elif A[i] + A[j] > t:
        break

print twosum(A,t)
