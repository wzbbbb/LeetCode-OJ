s='hello world sdflkjl;ksdf'

def length_last_word(s):
  res = 0
  n = len(s)
  for i in range(n-1,-1,-1):
    if s[i] != ' ': 
      res += 1
    else: 
      break
  return res
print  length_last_word(s)

