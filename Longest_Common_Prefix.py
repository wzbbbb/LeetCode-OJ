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

# Submission Result: Accepted
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pre = ''
        n = len(strs)
        if n == 0: 
            return ''
        min1 = len(strs[0])
        for s in strs:
            k = len(s)
            if min1 > k:
                min1 = k
        for i in range(min1):
            for j in range(1, n):
                if strs[j][i] != strs[j-1][i]:
                    return pre
            pre += strs[0][i]
        return pre
