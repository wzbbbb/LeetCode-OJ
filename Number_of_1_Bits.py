# Submission Result: Accepted 
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

