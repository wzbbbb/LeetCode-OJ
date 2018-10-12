haystack = 'BCCCEEACE'
needle = 'CE'

def find(haystack, needle):
  n = len(needle)
  m = len(haystack)
  for i in range(m - n + 1):
    if haystack[i : i+ n] == needle :
      return i
print find(haystack, needle)

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)
        if m == 0:
          return 0
        for i in range(n - m + 1):
          if haystack[i:i+m] == needle:
            return i
        return -1
