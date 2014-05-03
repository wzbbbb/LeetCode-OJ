class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
  def searchInsert(self, A, target):
    n=len(A)
    if n==0: return 0
    else:
      for i in range(n):
        if A[i] == target: return i
        if A[i] > target: return i
      return n  

