# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

#Submission Result: Accepted
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        p = 0
        q = n
        res = {}
        while p <= q:
            m = (p + q)//2
            res[m] = isBadVersion(m)
            res[m-1] = isBadVersion(m-1)
            res[m+1] = isBadVersion(m+1)
            if res[m]:
                q = (p + q)//2 - 1
            else:
                p = (p + q)//2 + 1
            if m -1 in res.keys() and m in res.keys():    
                if not res[m-1] and res[m]:
                     return m

