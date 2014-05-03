class Solution:
    # @return a string
  def longestCommonPrefix(self, strs):
    n=len(strs)
    if n==0: return ''
    pref=strs[0]
    for i in range(1,n):
      while len(pref)>0:
        lp=len(pref)
        if pref==strs[i][:lp]: break
        else: pref=pref[:lp-1]
    return  pref

