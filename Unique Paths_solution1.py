class Solution:
    # @return an integer
  def uniquePaths(self, m, n):
    if m==1 and n==1: return 1

    di=dict()
    m+=1
    n+=1
    di[(m-1,n-2)]=1
    di[(m-2,n-1)]=1
    x=max(m,n)
    k=2
    while k<x:
      i=0
      while i<k:
        if m-i <m-1:
          di[(m-1-i,n-1-k)]=di[(m-i,n-1-k)] +di[(m-1-i,n-k)]
        elif m-i==m-1: di[(m-1-i,n-1-k)]=1
        if n-i <n-1:
          di[(m-1-k,n-1-i)]=di[(m-k,n-1-i)] +di[(m-1-k,n-i)]
        elif n-i==n-1: di[(m-1-k,n-1-i)]=1
        i+=1
      di[(m-1-k),(n-1-k)] =di[(m-k),(n-1-k)] +di[(m-1-k),(n-k)]
      k+=1
      #print x,i,k
    #print di
    return di[(0,0)]      

