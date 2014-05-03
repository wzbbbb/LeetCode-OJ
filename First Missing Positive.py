class Solution:
    # @param A, a list of integers
    # @return an integer
  def firstMissingPositive(self, A):
    n=len(A)
    if n==0: return 1
    if n==1 and A[0] !=1: return 1
    elif n==1 and A[0] ==1: return 2
    for i in range(1,n+2):
      if i not in A: return i

