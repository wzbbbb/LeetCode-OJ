class Solution:
    # @return an integer
  #def uniquePaths(self, m, n):
  def uniquePaths(self, m, n,i=0,j=0, di=dict()):
    d=dict()
    d[(0,0)]=1
    for i in range(0,m):
      for j in range(0,n):
        if i==0: d[(i,j)] =1
        elif j==0: d[(i,j)] =1
        else: d[(i,j)]=d[(i-1),j] + d[(i,j-1)] 
    return  d[(m-1,n-1)]

