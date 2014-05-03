class Solution:
    # @param ratings, a list of integer
    # @return an integer
  def candy(self, ratings):
    A=ratings
    n=len(A)
    cnt=[1]*n
    cnt1=[1]*n
    cnt2=[1]*n
    for i in range(1,n):
        if A[i] > A[i-1] :  # ascending, left -> right
            cnt1[i]=cnt1[i-1]+1
        else: cnt1[i]=1
    for j in range(n-2,-1,-1):
        if A[j] > A[j+1] :  # ascending right to left 
            cnt2[j]=cnt2[j+1]+1
        else: cnt2[j]=1
    #print cnt1
    #print cnt2
    for i in range(n):
        cnt[i]=max(cnt1[i],cnt2[i])
    #print cnt
    return sum(cnt)

