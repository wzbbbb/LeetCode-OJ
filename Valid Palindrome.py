class Solution:
    # @param s, a string
    # @return a boolean
  def isPalindrome(self, s):
    dic=['a','b','c','d','e', 'f','g','h','i','j', 'k','l','m','n','o', 'p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E', 'F','G','H','I','J', 'K','L','M','N','O', 'P','Q','R','S','T','U','V','W','X','Y','Z', '0','1', '2','3','4','5','6', '7','8','9']
    n=len(s)
    i,j=0,n-1
    while i < n:
      if s[i] not in dic: i+=1; continue
      if s[j] not in dic: j-=1; continue
      if s[i].upper() !=s[j].upper() : return False
      else : 
        i +=1
        j-=1

    return True

