class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
  def rotate(self, matrix):
    n=len(matrix)
    if n==0: return []
    for i in range(n//2):
      for j in range(n):
        matrix[i][j],matrix[n-i-1][j] =matrix[n-i-1][j], matrix[i][j]
    #print matrix
    for i in range(n):
      for j in range(i+1):
        matrix[i][j],matrix[j][i] =matrix[j][i], matrix[i][j]
    return matrix

