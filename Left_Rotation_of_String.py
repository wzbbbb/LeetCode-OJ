s = 'abcdefg'
n = 2
def rotate(s, n):
  res = s[n:]
  res += s[:n]
  return res
print rotate(s,n)

