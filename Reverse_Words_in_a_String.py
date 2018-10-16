s = "    the   sky   is   blue  "
def reverse_word(s):
  A = s.split()
  res = ''
  for a in A[::-1]:
    res += a + ' '
  return res[:-1]

print s
print reverse_word(s) + '==='

def reverse(s):
  s1 = s.strip()
  n = len(s1)
  word, res = '', ''
  if len(s1) < 2: 
    return s1
  for i in range(n-1, -1, -1):
    if s1[i] != ' ':
      word += s1[i]
    elif word != '':
      res += word[::-1] + ' '
      word = ''
  if word != '':
    res += word[::-1] + ' '
  return res[:-1]

print reverse(s) 

def rev_rev(s):
  s1 = s[::-1].strip()
  res, word = '', ''
  for ss in s1:
    if ss == ' ':
      if word != '':
        res += word[::-1] + ' '
        word = ''
    else:
      word += ss
  res += word[::-1]
  return res
print rev_rev(s)

def rev_list(s):
  s1 = s[::-1].split()
  res = ''
  for ss in s1:
    if ss != ' ':
      res += ss[::-1] + ' '
  return res[:-1]
print rev_list(s)
