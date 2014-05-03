class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
  def spiralOrder(self, matrix):
    m=len(matrix)
    res=[]
    if m==0 : return []
    elif m==1: return matrix[0]
    n=len(matrix[0])
    if n==1: 
      for i in range(m):
        res.append(matrix[i][0]) 
      return  res
    bbi,bei=0,m   # bi: boarder for i; bj: boarder for j
    bbj,bej=0,n
    while bei >bbi and bej >bbj: 
      for j in range(bbj, bej):
        res.append(matrix[bbi][j])
      #print '==',res
      bbi+=1
      if bbj < bej:
        for i in range(bbi,bei):
          res.append(matrix[i][bej-1])
        #print res
        bej-=1
      #print bej,bbj, bbi,bei
      if bbi < bei:
        for j in range(bej-1, bbj-1, -1):
          res.append(matrix[bei-1][j])
        #print '++',res
        bei-=1
      if bbj < bej:
        for i in range(bei-1, bbi-1, -1):
          res.append(matrix[i][bbj])
        #print '-',res
        bbj+=1
    return res

