A = [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ],
     [ 10, 11, 12 ],
     [ 13, 14, 15 ]
    ]

#A = [
#     [ 1, 2, 3, 4],
#     [ 5, 6, 7, 8],
#     [ 9, 10, 11, 12],
#     [ 13, 14, 15, 16]
#    ]
def spiral(A):
  m = len(A)
  n = len(A[0])
  B = []
  for k in range(max(m,n) - 1):
    for i in range(k, n-k):
      B.append(A[k][i])
    for j in range(k+1, m-k):
      B.append(A[j][n-k-1])
    for p in range(n-k-2, k-1, -1):
      if m - k - 1 == k: break
      B.append(A[m-k-1][p])
    for q in range(m-k-2, k, -1):
      if n-k-1 == k: break
      B.append(A[q][k])
  return B
for a in A:
  print a
print spiral(A)

