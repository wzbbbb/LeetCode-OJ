#A = [3,4,6,9,9]
A = [3,4,6,9,0]
def plus_one(A):
  n = len(A)
  print A
  A.reverse()
  up = 1
  for i in range(n):
    if A[i] + up == 10:
      A[i] , up = 0 , 1
    else:
      A[i] = A[i] + up
      up = 0
  A.reverse()
  return A

print plus_one(A)

# Submission Result: Accepted
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ''
        res = []
        for n in digits:
            s += str(n)
        str1 = str(int(s) +1)
        for ss in str1:
            res.append(int(ss))
        return res
