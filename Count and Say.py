class Solution:
    # @return a string
  def countAndSay(self, n):
    res,cnt='1',0
    if n==1: return  res
    for i in range(1,n):
      m=len(res)
      cnt=0
      tmp=''
      for j in range(m):
        cnt+=1
        #print(res, res[j])
        if j +1 <m : 
          if res[j+1]==res[j]: continue
            #print('--',j,res[j],cnt)
          elif res[j+1]!=res[j]: 
            tmp+=str(cnt) + res[j]
            cnt=0
        else:  
            tmp+=str(cnt) + res[j]
            cnt=0
      res=tmp
      #print('++',res)
    return res  

