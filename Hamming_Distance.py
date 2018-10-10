# Submission Result: Accepted  100% :D
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        n = x ^ y
        s = bin(n)
        count = 0
        for s1 in s:
            if s1 == '1':
                count += 1
        return count

