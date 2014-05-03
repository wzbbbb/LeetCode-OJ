class Solution:
    # @return a boolean
  def isPalindrome(self, x):
    s=str(x)
    #print(s[::-1], s) 
    if s==s[::-1]: return True
    else: return False

