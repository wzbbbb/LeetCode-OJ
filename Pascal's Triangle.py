class Solution:
    # @return a list of lists of integers
  def generate(self, n):
    A=[]
    for i in range(n):
      row=[]
      for j in range(0, i+1):
        if j -1 >=0 and j +1 <= i:
          s=A[i-1][j-1] + A[i-1][j]
          row.append(s)
        elif j-1<0 or j+1> i :
          row.append(1) 
      A.append(row)
    #return A, row
    return A 

