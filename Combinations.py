class Solution:
    # @return a list of lists of integers
  def combine(self, n, k):
    res=[[]]
    for i in range(1,n+1):
      tmp=[]
      for r in res:
        tmp.append(r+[i])
      res+=tmp[::]
    out=[]
    for r in res:
      if len(r)==k: out.append(r)
    return out

