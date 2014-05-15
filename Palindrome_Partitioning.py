class Solution:
    # @param s, a string
    # @return a list of lists of string
  #def partition(self, s):
  def partition(self, s, startp=None,res=None,tmp=None):
    if startp==None: startp=0
    if res==None: res=[]
    if tmp==None: tmp=[]
    n=len(s)
    if startp ==n: 
      res.append(tmp[::])
      return res
    for i in range(startp+1,n+1):
      if s[startp:i] == s[startp:i][::-1]: 
        tmp.append(s[startp:i])
        res=self.partition(s, i, res,tmp)
        tmp.pop()
    return res      
