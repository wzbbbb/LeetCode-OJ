class Solution:
    # @return an integer
  def reverse(self, x):
    if x <0: neg=True; x=abs(x)
    else: neg=False
    n1,rev,out=x,0,0
    while n1 !=0: 
      dig=n1%10
      rev=rev* 10 + dig
      n1=n1/10
    if neg==True: return rev * (-1)
    else: return rev

