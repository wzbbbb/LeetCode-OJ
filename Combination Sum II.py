class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
  def combinationSum2(self, candidates, target):
    cas=sorted(candidates)
    n=len(cas)
    res=[]
    tmp=[[]]
    tmp2=[[]]
    for i in range(0,n):
      #print('ca',cas[i])
      if i >0:
        if cas[i] == cas[i-1]: 
          tmp2=tmp1[::]
        else:
          tmp2=tmp[::]
      #print('tmp',tmp,'tmp2',tmp2)
      tmp1=[]
      for t in tmp2:
        #print('===t',t)
        tmp1.append(t[::])
        tmp1[-1].append(cas[i])
        #print('----',tmp[-1],'attached',cas[i])
        st=sum(tmp1[-1]) 
        if st ==target: res.append(tmp1[-1])
        if st>target: 
          #print('tmp1 pop', tmp1[-1])
          tmp1.pop()  
          #break
      tmp+=tmp1[::]
      tmp2=tmp[::]
      #print('tmp1',tmp1,'tmp',tmp)
    return res

