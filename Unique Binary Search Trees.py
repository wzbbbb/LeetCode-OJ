class Solution:
    # @return an integer
  def numTrees(self, n):
    #DP(i) = 2*DP(i-1) + 2*DP(i-2) + DP(j)*DP(i-j-1) ... i>=0
    #DP(5) = 2*DP(4)+ 2*DP(3) + DP(2)*DP(2)
    #DP(7) = 2*DP(6)+ 2*DP(5) + DP(2)*DP(4) + DP(3)*DP(3) + DP(4)*DP(2)
    DP=[0] *(n+3)
    DP[0]=1
    DP[1]=2
    DP[2]=5
    for i in range(3,n):
      DP[i]+=2*DP[i-1]  
      DP[i]+=2*DP[i-2]  
      for j in range(2,i-1):
        #print('here',DP[i])
        if i-j>=2:
          DP[i]+=DP[j-1]*DP[i-1-j]  
          #print('there',DP[i],DP[j-1],DP[i-1-j]  )

    return DP[n-1]

