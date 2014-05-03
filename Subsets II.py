class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
  def subsetsWithDup(self, S):
    A=sorted(S)
    res,prea=[[]],None
    for a in A:
      n=len(res)
      if a!=prea:
        for i in range(n): 
          tmp=res[i][::]
          tmp.append(a)
          res.append(tmp)
      else:
        for i in range( pren, n): 
          tmp=res[i][::]
          tmp.append(a)
          res.append(tmp)
      prea=a
      pren=n
    #print(len(res),res)
    return res

