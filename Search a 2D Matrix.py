class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
  def searchMatrix(self, matrix, target):
    if len(matrix) >0:
      n=len(matrix[0])
    else: return False
    for ma in matrix:
      if target in ma: return True
      elif target < ma[-1]:
        return False
    return False

