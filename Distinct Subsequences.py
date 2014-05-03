class Solution:
    # @return an integer
  def numDistinct(self, S, T):
    # 2 moves, 
    # 1). if S[j] ==T[i]: i+1, j+1 
    # 2). if S[j] !=T[i]: i, j+1
    #  if S[j]==T[i]: DP(i,j) =DP(i,j-1) +DP(i-1,j-1)
    # The valid sequence from (i-1,j-1) and (i,j-1) got here both valid
    # if S[j]!=T[i]: DP(i,j) = DP(i,j-1)
    # The move is j+1. The valid sequence hold to find T[i]
    # When the first char show up, DP(i,j) +=1
    #     r a b b b i t r a t
    #   0 1 1 1 1 1 1 1 1 1 1 # DP(-1,j) =1, DP (i,-1) =0 
    # r 0 1 1 1 1 1 1 1 2 2 2
    # a 0 0 1 1 1 1 1 1 1 3 3
    # b 0 0 0 1 2 3 3 3 3 3 3
    # b 0 0 0 0 1 3 3 3 3 3 3
    # i 0 0 0 0 0 0 3 3 3 3 3
    # t 0 0 0 0 0 0 0 3 3 3 6
    m=len(T)
    n=len(S)
    if n<m or n==0 or m==0: return 0
    dp=[[0 for i in range(n)] for j in range(m)]
    for i in range(m):
      for j in range(i, n):
        if S[j] == T[i]: 
          if i==0: dp[i][j] = 1 + dp[i][j-1]
          else: dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
        else: 
          if j==0: dp[i][j] = 0
          else: dp[i][j] = dp[i][j-1]
    return dp[m-1][n-1]

