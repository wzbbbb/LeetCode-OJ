class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
  def sortColors(self, A):
    leng=len(A)
    if leng<2 : return A

    last_0=None
    first_2=None
    i=0
    while  i < leng: # put 0 in front; put 2 at the end; see 1, pass
      #print i, A[i], A
      if A[i] ==0: 
        if last_0==None :  last_0=0 
        while A[last_0] ==0:
          last_0+=1
          if last_0 >=leng: return A
        if i< last_0: i=last_0
        #print '--',i, last_0  
        A[i],A[last_0] = A[last_0],A[i] 
      elif A[i] ==2 :
        if first_2==None: 
          first_2= leng-1
        else: first_2-=1
        if first_2 > i:
          while A[first_2] ==2:
            first_2-=1
            if  first_2 <=0: return A
          #print 'i, first_2', i, first_2
          if first_2 > i:A[i],A[first_2] = A[first_2],A[i] 
        else:  break
      elif A[i]==1: i+=1
    return A

