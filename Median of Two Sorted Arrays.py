class Solution:
    # @return a float
  def findMedianSortedArrays(self, A, B):
    res=[]
    while A and B:
      if A[-1] >= B[-1]:
        res.append(A.pop())
      else:
        res.append(B.pop())
    res.reverse()
    res= A + B + res
    n=len(res)
    if n%2==0: return (res[n//2 -1] + res[n//2]) /2.0
    else:  return res[n//2]

