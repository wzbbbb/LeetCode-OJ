class Solution:
    # @return a list of integers
  def getRow(self, n):
    pre_row=[]
    n+=1
    for i in range(n):
      row=[]
      for j in range(0, i+1):
        if j -1 >=0 and j +1 <= i:
          #print(j)
          s=pre_row[0][j-1] + pre_row[0][j]
          row.append(s)
        elif j-1<0 or j+1> i :
          row.append(1) 
      if i==n-1: return row #, pre_row
      pre_row=[]
      pre_row.append(row)      

