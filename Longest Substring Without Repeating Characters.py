class Solution:
    # @return an integer
 def lengthOfLongestSubstring(self, s,startp=0,res=0,st=''):
  n=len(s)
  #print(s)
  for i in range(startp +1,n):
    #print('++',s[i] ,s[startp:i]), len(s[startp:i])
    while s[i] in s[startp:i]:
      if i-startp > res:
        res=i- startp
        #st= s[startp:i]
        #print('--',res,st)
      startp+=1
      if startp ==i: break 
    if i==n-1 and s[i] not in s[startp:i]: 
      if i-startp+1 > res:
        res=i-startp +1
      #st=s[startp:]
  if res==0 and n !=0: 
    res=n
    #st=s
  #print(res,st)
  return res

