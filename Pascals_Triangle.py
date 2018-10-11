''' B[i] = A[i-1] + A[i]        '''
n = 5
def pascal_triangle(n):
  A = [1,1]
  if n < 1 : return None
  if n == 1 : return [1]
  if n == 2 : return [1,1]
  for i in range(2, n+1):
    B = [0] * (i+1)
    for j in range(i+1):
      if j == 0 or j == i: 
        B[j] = 1
        continue
      B[j] = A[j-1] + A[j]
    print B
    A = B[:]
  return B
print  pascal_triangle(n)

#Submission Result: Accepted  100% :D
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(numRows):
            tmp = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    tmp.append(1)
                else:
                    tmp.append(res[i-1][j-1] + res[i-1][j])
            res.append(tmp)
        return res
