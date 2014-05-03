class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
  def searchRange(self, A, target):
    n=len(A)                                   
    if target not in A: return [-1,-1]
    if n == 1 and target in A : return [0,0]
    lf=self.l_limit(A,target)
    rt=self.r_limit(A,target)
    return [lf,rt]

  def l_limit(self,A,target,shf=0,res=None):
    n=len(A)
    m=n//2
    #print(A[m])
    if A[m] ==target and m==0 : return 0
    elif A[m] == target and A[m-1] <target: return shf+m
    elif A[m] == target and A[m-1] ==target: 
      res=self.l_limit(A[:m], target,shf,res)
    elif A[m] < target:res=self.l_limit(A[m:], target,shf+m,res)
    elif A[m] > target: res=self.l_limit(A[:m], target,shf,res)
    return res

  def r_limit(self,A,target,shf=0,res=None):
    n=len(A)
    m=n//2
    #print('--',A[m])
    if A[m] ==target and m==n-1 : return shf+n-1
    elif A[m] == target and A[m+1] > target: return shf+m
    elif A[m] ==target and A[m+1] == target:
      res=self.r_limit(A[m:], target,shf+m,res)
    elif A[m] < target : res=self.r_limit(A[m:], target,shf+m,res)
    elif A[m] > target : res=self.r_limit(A[:m], target,shf,res)
    return res

