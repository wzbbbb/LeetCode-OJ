class Solution:
    # @param A, a list of integers
    # @return an integer
  def trap(self, A):
    n=len(A)
    if n<=2: return 0
    res,que= self.calc(A)
    #print que
    if len(que)<=2: return res
    res1,que1= self.calc(que[::-1])
    res+=res1
    return res
  def calc(self,A):
    n,res,que=len(A),0,[]
    if n<=2: return 0,[]
    que.append(A[0])
    for i in range(1,n):
      #print '===+',que[0]
      if A[i] < que[0]:
        que.append(A[i])
      else:
        m=len(que)
        res+= (m-1)* que[0]
        #print '--',que,res,'A[i]',A[i]
        for j in range(1,m):
          res-=que[j]
        que=[]; que.append(A[i])
        #print '==',res, A[i], m, que
    #print que
    return res,que

