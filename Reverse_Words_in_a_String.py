s = "    the   sky   is   blue  "
def reverse_word(s):
  A = s.split()
  res = ''
  for a in A[::-1]:
    res += a + ' '
  return res[:-1]

print s
print reverse_word(s) + '==='
