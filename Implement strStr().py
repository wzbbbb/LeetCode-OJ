class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
  def strStr(self, haystack, needle):
    m=len(needle)
    n=len(haystack)
    if n==0 and m==0: return ''
    for i in range(n):
      #print '--',haystack[i:m+i]
      if m+i <=n:
        if haystack[i:m+i] ==needle: 
          return haystack[i:]

