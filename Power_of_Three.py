# Submission Result: Accepted
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        k = 3
        while True:
            if n > k :
                k = k * 3
            elif n == k:
                return True
            else :
                return False
