class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
  def merge(self, A, m, B, n):
    #if m==0 and n==0: return []
    #elif m==0 : return B
    #elif n==0 :return A
    i=m -1
    j=n -1
    #A=A + [0]*n
    k=m+n -1
    #print A, B
    while i >=0 and j >=0:
        #print B[j] , A[i]
        if B[j] >A[i]: 
            A[k]=B[j]
            j-=1
        else: 
            A[k]=A[i]
            i-=1
        k-=1
    if j >= 0: 
        for h in range(j+1):
            A[h]=B[h]

