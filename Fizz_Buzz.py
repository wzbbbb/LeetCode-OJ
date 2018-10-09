# Submission Result: Accepted 
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = [0]*n
        for i in range(1,n+1):
            if i % 15 == 0:
                res[i-1] = 'FizzBuzz'
                continue
            if i % 3 == 0:
                res[i-1] = 'Fizz'
                continue
            if i % 5 == 0:
                res[i-1] = 'Buzz'
                continue
            res[i-1] = str(i)
        return res
