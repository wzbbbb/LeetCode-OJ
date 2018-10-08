# Submission Result: Accepted, the fastest one, 100% :D
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str.strip()
        n = len(s)
        if n == 0:
            return 0
        res, sign = '', 1
        if s[0] == '-':
            sign = -1
        elif s[0].isdigit():
            res = s[0]
        elif s[0] != '+':
            return 0
        for i in range(1,n):
            if s[i].isdigit():
                res += s[i]
            else:
                break
        if res == '':
            return 0
        if int(res) * sign < 2**31 * (-1):
            return 2**31 * (-1)
        elif int(res) * sign > 2**31 -1:
            return 2**31 -1
        else:
            return int(res) * sign
