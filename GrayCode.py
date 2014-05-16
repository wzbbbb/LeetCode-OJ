class Solution:
    # @return a list of integers
  def grayCode(self, n, factors=None,out=None,res=None):
    # ^ the last number in res with a number of pow(2,i)
    # try the small number first, the 1111 last
    if n==0 : return [0]
    if factors==None: 
      out=[]; res=[0]; factors=[0]
      for i in range(n):
        factors.append(pow(2,i))
    while len(res) < pow(2,n):
      for f in factors: 
        p= res[-1] ^f
        if p not in res:
          res.append(p)
          break
          #res=self.grayCode(n,factors,out,res)
    #time.sleep(1)
    return res
