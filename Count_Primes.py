#Submission Result: Accepted, but very slow :(
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        prime = [2]
        for i in range(3,n):
            k = int(i**0.5)+1
            isprime = False
            for p in prime:
                if p > k: 
                    break
                elif i % p == 0:
                    isprime = False
                    break
                else:
                    isprime = True
            if isprime:
                prime.append(i)
        return len(prime)
