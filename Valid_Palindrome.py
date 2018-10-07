S = 'A man, a plan, a canal: Panama '
#S = "race a car"
#S = ''
def validate(S):
  res = ''
  for s in S:
    if s.isalpha():
      res += s.lower()
  return res == res[::-1]

print  validate(S)


# Submission Result: Accepted
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        t = ''
        for s1 in s.lower():
            if s1.isalpha() or s1.isdigit():
                t += s1
        return t == t[::-1]
