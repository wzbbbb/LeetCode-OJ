class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
  #def pow(self, x, n):
  def power(self,x,n):
    if n==0 :return 1
    #print x,n
    v=self.power(x,n/2)
    if n%2==0: return v*v
    else: return v*v*x

  def pow(self, x, n):
    o,v=1,1
    if x==0: return 0
    m=abs(n)
    o=self.power(x,m)
    if n<0: return 1.0/o
    return o

