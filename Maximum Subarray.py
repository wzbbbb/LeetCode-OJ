class Solution:
    # @param A, a list of integers
    # @return an integer
  def maxSubArray(self, A):
    res,summ=None,None
    for a in A:
      if summ==None: 
        summ=a
      elif a<0:
        if a > summ: summ=a
        elif summ +a > 0 : summ+=a
        else: summ=None
      elif a>=0:
        if summ<0: summ=a
        else :summ+=a
      if res==None or summ> res: res=summ
    return res

