s='hello world'

def no_repeat_substr(s):
  res = []
  length = 0
  for c in s:
    if c not in res:
      res.append(c)
      n = len(res)
      print res
      if n > length: 
        length = n
    else: 
      res.reverse()
      while c in res:
        res.pop()
      res.reverse()
      res.append(c)
  return length, res

print no_repeat_substr(s)

