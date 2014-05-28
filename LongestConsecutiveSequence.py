class Solution:
    # @param num, a list of integer
    # @return an integer
  def longestConsecutive(self, num):
    seq=sorted(num)
    max=1; tmp=1
    n=len(seq)
    for i in range(1,n):
      #print tmp
      if abs(seq[i-1] - seq[i]) == 1:
        tmp+=1
      elif seq[i-1] == seq[i] :  continue
      else: 
        if tmp > max: max=tmp
        tmp=1
    if max< tmp: return tmp
    return max
