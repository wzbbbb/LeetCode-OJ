haystack = 'BCCCEEACE'
needle = 'CE'

def find(haystack, needle):
  n = len(needle)
  m = len(haystack)
  for i in range(m - n + 1):
    if haystack[i : i+ n] == needle :
      return i
print find(haystack, needle)

