class Solution:
    # @param A a list of integers
    # @return an integer
  def removeDuplicates(self, A):
    n,i=len(A),0
    if n <2: return n
    while i < n:
      if i >1: 
        if A[i]== A[i-1] and A[i]==A[i-2]: 
          A.pop(i)
          #print 'here'
          i-=1
      i+=1
      n=len(A)
      #print '--',n
    #print A
    return len(A)

