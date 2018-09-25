A=['asdrsdfle','asdrrrrfe','asdrfe']
def longest_common_prefix(A):
  n = len(A)
  res, tmp='', ''
  for a in A[0]:
    tmp += a
    j = len(tmp)
    for i in range(n):
      if A[i][:j] != tmp: 
        return res
    res = tmp
  return res
print longest_common_prefix(A)
