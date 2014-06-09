class Solution:
    # @param A, a list of integers
    # @return an integer
  def jump(self, A):
    n=len(A)
    p1,p2=0 ,0
    jump=0;max=0
    if n==1: return 0
    if A[0] >= n-1: return 1
    while p1 < n-1:
      #print 'p1',p1, max, jump
      #if p1 >= n-1 : return jump
      max=0
      for i in range(p1+1, A[p1] + p1 +1):
        #print '--', i, max
        try:
          if max < A[i] + i:
            max= A[i] +i
            pos=i
        except IndexError:
          jump+=1
          return jump
      #print 'pos, max',pos, max
      p1= pos 
      jump+=1
      if max>=n-1: 
        jump+=1
        return jump
    return jump
