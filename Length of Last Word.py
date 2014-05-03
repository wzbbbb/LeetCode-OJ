class Solution:
    # @param s, a string
    # @return an integer
  def lengthOfLastWord(self, s):
    if len(s) == 0 : return 0
    res=s.split()
    if len(res) == 0: return 0
    return len(res[-1])

