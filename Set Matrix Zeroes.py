class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
  def setZeroes(self, matrix):
    rec=[]
    m=len(matrix)
    if m==0: return 
    n=len(matrix[0])
    for i in range(m):
      for j in range(n):
        if matrix[i][j] ==0: rec.append((i,j))

    for r in rec:
      for j in range(n):
        matrix[r[0]][j]=0
      for i in range(m):
        matrix[i][r[1]]=0

