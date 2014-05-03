class Solution:
    # @param an integer
    # @return a list of string
  def generateParenthesis(self, n):
    res=["()"]
    if n==0: return ''
    if n==1: return res
    for i in range(1,n):
      tmp=[]
      for r in res: 
        for j in range(len(r)):
          s=''
          s+=r[:j] + '()' + r[j:]
          #print(s)
          if s not in tmp:
            tmp.append(s)
      res=tmp
    #print(res)
    return res
        

