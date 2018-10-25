# Submission Result: Accepted  100%  :)
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = bin(n)
        count = 0
        m = len(s)
        for i in range(2,m):
            if s[i] == '1':
                count +=1
        return count

# Submission Result: Accepted , this is a cool solution, but slower though 60% ?
# shift left
n = 100
def number_of_1(n):
  i, res = 1 , 0
  while i <= n:
    if n & i != 0:
      res +=1
    i = i << 1
  return res
print number_of_1(n)

# Submission Result: Accepted , this is a cool solution, but slower, around 80% 
def shift_right(n):
  res = 0
  while n > 0:
    if n & 1 == 1:
      res += 1
    n = n >> 1
  return res
print shift_right(n)
    

