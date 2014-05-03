class Solution:
    # @param a list of integers
    # @return an integer
  def removeDuplicates(self, A):
    i=0
    while i +1 < len(A):
      if  A[i] == A[i+1] : A.pop(i)
      else: i+=1
    return len(A)


