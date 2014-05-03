class Solution:
    # @return a string
  def convert(self, s, nRows):
    n=nRows
    res=['' for i in range(n)]
    leng=len(s)
    i,out=0,''
    mov='down'
    if n==1: return s
    for j in range(leng):
      if i+1< n and mov=='down':
        res[i]+=s[j]
        i+=1
      elif i> 0 and mov=='up':
        res[i]+=s[j]
        i-=1
      elif i +1 ==n :
        res[i]+=s[j]
        i-=1;  mov ='up'
      elif i ==0  :
        res[i]+=s[j]
        mov='down'
        i+=1
    for r in res:
       out+=r
    return out

