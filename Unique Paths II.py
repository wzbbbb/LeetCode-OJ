class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
  def uniquePathsWithObstacles(self, obstacleGrid):
    d=dict()
    ob=obstacleGrid
    m=len(ob)
    n=len(ob[0])
    if m==1 and n==1 and obstacleGrid[m-1][n-1] ==0 :return 1
    if obstacleGrid[0][0] ==1 : return 0
    else: d[(0,0)] =1
    for i in range(0,m):
      for j in range(0,n):
        if ob[i][j]==1: d[(i,j)] =0
        elif i==0 and j>0: d[(i,j)] = d[(i,j-1)]
        elif j==0 and i>0: d[(i,j)] =d[(i-1,j)]
        elif (i,j) not in d.keys(): d[(i,j)]=d[(i-1),j] + d[(i,j-1)] 
    return  d[(m-1,n-1)]

