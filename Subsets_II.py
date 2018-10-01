S = [1,2,2,3]
def subsetII(S):
  res = [[]]
  for s in S:
    tmp = []
    for r in res:
      if r + [s] not in res:
        tmp.append( r + [s])
    res += tmp
  return res
print subsetII(S)

