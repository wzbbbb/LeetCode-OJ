#path = "/home/", => "/home"
#path = "/a/./b/../../c/", => "/c"
#path = "/a/./b/../../c/"
path = "/abc/.././."
def simplify(path):
  ''' It is a stack operation
  '''
  res = []
  stack = path.split('/')
  for s in stack:
    if s == '.': continue
    if s == '..' and res:
      res.pop()
      continue
    res.append(s)

  if path[:1] == '/':
    out = '/'
  else:
    out = ''
  for r in res[::-1]:
    out += r
  return out
print simplify(path)
