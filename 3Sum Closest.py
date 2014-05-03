class Solution:
    # @return an integer
  def threeSumClosest(self, num, target):
    A=sorted(num)
    n,dist=len(A),None
    for i in range(n):
      j,k=i+1,n-1
      while j < k:
        summ=A[i] + A[j] +A[k]
        dif=target-summ
        if dif ==0: return target
        if dif > 0: j+=1
        if dif <0 : k-=1
        cdist=abs(dif)
        if dist==None: 
          dist=cdist
          res=summ
        elif cdist < dist:  
          res=summ 
          dist=cdist
    return res

