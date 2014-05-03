class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
  def plusOne(self, digits):
    n=len(digits)
    adv=1
    for i in range(n-1,-1,-1):
      if digits[i] ==9 and adv==1: 
        digits[i] =0
        adv=1
      elif digits[i] <9 and adv==1:
        digits[i]+=1
        adv=0
    if adv==1:
      digits.reverse()
      digits.append(1)
      digits.reverse()
    return digits

