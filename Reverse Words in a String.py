class Solution:
    # @param s, a string
    # @return a string
  def reverseWords(self, s):
    A,res=[],''
    A=s.split()
    A.reverse()
    n=len(A)
    for i in range(n): 
      if i == n-1: res+=A[i]
      else: res+=A[i] + ' '
    return res

