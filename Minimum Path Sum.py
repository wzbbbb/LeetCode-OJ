class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
  def minPathSum(self, grid):
    #DP(i,j)=min(DP(i-1,j), DP(i,j-1)) + grid[i][j]
    m=len(grid)
    if m==0: return 0
    n=len(grid[0])
    DP=[[0] *n]*m
    #DP[0][0]=grid[0][0]
    for i in range(m):
      for j in range(n):
        if i>0 and j >0:
          DP[i][j] = min(DP[i-1][j], DP[i][j-1]) + grid[i][j]
        elif i==0:
          DP[i][j] = DP[i][j-1] + grid[i][j]
        elif j==0:
          DP[i][j] = DP[i-1][j] + grid[i][j]
        elif i==0 and j==0:
          DP[i][j] =  grid[i][j]
    return DP[m-1][n-1]

