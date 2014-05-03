class Solution:
    # @return an integer
  def uniquePaths(self, m, n):
    di=dict()
    if m==1 and n==1: return 1
    di[(m-1,n-2)]=1
    di[(m-2,n-1)]=1
    x=max(m,n)
    k=1
    while k<x:
      i=0
      while i<k:
        if i >=1:
          di[(m-1-i,n-1-k)]=di[(m-i,n-1-k)] +di[(m-1-i,n-k)]
          di[(m-1-k,n-1-i)]=di[(m-k,n-1-i)] +di[(m-1-k,n-i)]
        elif i==0:
          di[(m-1-k,n-1-i)]=1
          di[(m-1-i,n-1-k)]=1
        i+=1
      di[(m-1-k,n-1-k)] =di[(m-k,n-1-k)] +di[(m-1-k,n-k)]
      k+=1
    #print di
    return di[(0,0)]   

