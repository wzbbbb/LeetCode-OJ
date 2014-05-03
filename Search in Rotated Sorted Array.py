class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
  def search(self, A, target):
    n=len(A)
    if n==0: return -1
    else: 
      if target >= A[0]:
        for i in range(n):
          if target > A[i] and i+1< n: 
            if A[i+1] > A[i]:
              continue
            else: return -1
          elif target > A[i] and i+1 >=n:
            return -1
          elif target ==A[i]: return i
          elif target < A[i] : return -1
      else:
        for i in range(n-1,-1,-1):
          if target >A[i] : return -1
          elif target ==A[i] : return i
          elif target < A[i] and i-1 >=0:
            if A[i-1] < A[i]: continue
            else: return -1
    return -1

