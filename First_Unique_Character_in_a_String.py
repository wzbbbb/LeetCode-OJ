# Submission Result: Accepted
''' adding all char to a set, if the set size does not increase,
    that's a duplicate, remove it from the result
'''
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        c = set()
        res = []
        for i in range(n):
            m = len(c)
            c.add(s[i])
            if len(c) == m + 1:
                res.append(s[i])
            else:
                if s[i] in res:
                    res.remove(s[i])
        if len(res) == 0: 
            return -1
        for i in range(n):
            if s[i] == res[0]:
                return i
