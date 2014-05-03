class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
  def minimumTotal(self, triangle): # dp(i,j)=min(dp(i-1,j), dp(i-1,j-1)) + triangle[i][j]
    # only keep the last line of dp, dp(i-1,x), so space O(n)
    n=len(triangle[-1])
    dp=[[0 for i in range(n)] for j in range(2)]
    for i in  range(len(triangle)):
      for j in range(len(triangle[i])):
        #print 'i,j', i,j
        if i==0 : dp[1][j]=triangle[i][j]
        elif i!=0 and j==0: dp[1][j]= triangle[i][j] + dp[0][j]
        elif i==j : dp[1][j]= triangle[i][j] +  dp[0][j-1]
        else: dp[1][j]= triangle[i][j] + min(dp[0][j] , dp[0][j-1])
        #print dp
      dp[0]=dp[1]; dp[1]=[0 for i in range(n)]
    return min(dp[0])

