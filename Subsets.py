class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
  def subsets(self, S):
    A=sorted(S)
    res=[[]]
    for a in A:
      tmp=[]
      for r in res:
        tmp.append(r+[a])
      res+=tmp[::]
    return res

