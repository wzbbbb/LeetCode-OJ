class Solution:
    # @param n, an integer
    # @return an integer
  def climbStairs(self, n):
    cnt,p1,p2=1,1,0
    for i in range(n):
      cnt=p1+p2
      p2=p1
      p1=cnt
    return cnt

