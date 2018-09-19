s = '123456789abcdef'
nRows = 3
'''A better way to do this, form a list of string and attach new char to them
For example:
n = 5 =>  1,2,3,4,5,4,3,2
n = 4 => 1,2,3,4,3,2
'''

def convert(s, nRows):
  n=nRows
  leng=len(s)
  pattern_length = n + n - 2
  A = [''] * n
  pattern = []
  for i in range(n):
    pattern.append(i)
  for i in range(n-2, 0, -1):
    pattern.append(i)
  i = 0
  while i < leng:
    for j in range(pattern_length):
      A[pattern[j]] += s[i]
      i += 1
      if i == leng:  break 
  ss=''
  print A
  for a in A:
    ss += a
  return ss
print s
print convert(s, nRows)
