A = [
     [2],
    [3,4],
   [3,2,7],
  [4,2,6,3],
 [5,7,5,1,3]
]
n = len(A)
def min_path_sum(A, n, sum1=0, min_sum=None, i=0, j=0):
  ''' recursive, working like a complete binary tree
  ''' 
  if i >= n:
    if min_sum == None or sum1 < min_sum:
      min_sum = sum1
  else:
    sum1 += A[i][j]
    min_sum = min_path_sum(A, n, sum1, min_sum, i+1, j)
    min_sum = min_path_sum(A, n, sum1, min_sum, i+1, j+1)
  return min_sum
print min_path_sum(A,n)
