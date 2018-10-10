# Submission Result: Accepted
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = bin(n)[2:][::-1]
        k = 32 - len(s)
        return int(s + '0' * k, 2)
