s = 'abaccdeff'
''' 2 ways to do it,
    1. to form a new string/list, remove the duplicate ones, 
       and return first item
    2. use dict to count, and loop throug string 2nd time to find the first item
'''
def uniq(s):
  res = ''
  for s1 in s:
    if s1 not in res:
      res += s1
    else:
      i = res.find(s1)
      res = res[:i] + res[i+1:]
  return res[0]

def uniq_dict(s):
  res = {}
  for s1 in s:
    if s1 not in res.keys():
      res[s1] = 1
    else:
      res[s1] += 1
  for s1 in s:
    if res[s1] == 1:
      return s1
print uniq(s)
#print uniq_dict(s)


