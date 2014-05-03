class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
  def combinationSum(self, candidates, target):
    cas=candidates
    res,tmp=[],[]
    for ca in cas:
      if ca==target: res.append([ca])
      else: tmp.append([ca])
    #print(tmp)
    while True:
      tmp2=[]
      for t in tmp:
        for ca in cas:
          tmp1=[]
          #print(t)
          if ca >= t[-1]: 
            tmp1=t[::]
            tmp1.append(ca)
            #print('t=',t,ca,'tmp1',tmp1, 'res',res)
            if sum(tmp1)==target: res.append(tmp1[::])
            if sum(tmp1) < target and len(tmp1)>0: tmp2.append(tmp1[::])
      if len(tmp2) ==0: break
      tmp=tmp2[::]
      #print('++',tmp)
    return res

