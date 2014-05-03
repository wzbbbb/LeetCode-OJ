class Solution:
    # @return a list of lists of integer
  def generateMatrix(self, n):
    matrix=[[0 for i in range(n)] for j in range(n)]
    m=1
    bbi,bei,bbj,bej=0,n,0,n
    while m< n*n+1:
      i=bbi
      for j in range(bbj,bej):
        matrix[i][j]=m
        m+=1 
      bbi+=1
      j=bej-1
      for i in range(bbi,bei):
        matrix[i][j] =m
        m+=1
      bej-=1
      i=bei-1
      for j in range(bej-1, bbj-1, -1):
        matrix[i][j]=m
        m+=1
      bei-=1
      j=bbj
      for i in range(bei-1,bbi-1,-1):
        matrix[i][j]=m
        m+=1
      bbj+=1

    return matrix

