class Solution:
    # @return a tuple, (index1, index2)
  def twoSum(self, num, target):
  #print(num, target)
  #B=quicksort(num)
    B=sorted(num)
    n=len(B)
    for i in range(n):
      for j in range(i+1,n):
        t=B[i] + B[j]
        if  t== target: 
          x=num.index(B[i])
          if B[i] == B[j]:
            num.reverse()
            z=num.index(B[j])
            y=n-1-z
          else: y=num.index(B[j])
          if x > y: x,y=y,x
          #print("found",x+1,y+1)
          return (x+1,y+1)
          #print('no match')
    return (None,None)

