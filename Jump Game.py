class Solution:
    # @param A, a list of integers
    # @return a boolean
  def canJump(self, A):
    n=len(A)
    i=0
    while True:
      #print i
      if i>=n-1: return True
      if A[i] ==0 : return False
      i+=A[i]
    return False

