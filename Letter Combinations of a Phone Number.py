class Solution:
    # @return a list of strings, [s1, s2]
  def letterCombinations(self, digits):
    pad=[]
    pad.append([' '])
    pad.append(['&'])
    pad.append(['a','b','c'])
    pad.append(['d','e','f'])
    pad.append(['g','h','i'])
    pad.append(['j','k','l'])
    pad.append(['m','n','o'])
    pad.append(['p','q','r','s'])
    pad.append(['t','u','v'])
    pad.append(['w','x','y','z'])
    res=[]
    n=len(digits)
    if n==0: return ['']
    num=int(digits[0])
    for j in range(len(pad[num])):
      res.append(pad[num][j])
    for i in range(1,n):
      num=int(digits[i])
      #print(n,num, res)
      tmp=[]
      for r in res:
        kl=len(pad[num])
        #print('kl',kl)
        for k in range(kl):
          tmp.append(r+pad[num][k])
      res=tmp
      #print(res)
    #print(len(res), res)
    return res

