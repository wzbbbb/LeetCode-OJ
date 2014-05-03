class Solution:
    # @return an integer
  def romanToInt(self, s):
    n,num,skip=len(s),0,False
    for i in range(n):
      if skip: 
        skip=False
        continue
      if s[i]=='M': num +=1000
      elif s[i] =='C':
        if i+1 <n : 
          if s[i+1] == 'D': 
            num +=400
            skip=True
          elif s[i+1] == 'M': 
            num +=900
            skip=True
          else: num+=100
        else: num+=100
      elif s[i] =='X':
        if i+1 <n : 
          if s[i+1] == 'L': 
            num +=40
            skip=True
          elif s[i+1] == 'C': 
            num +=90
            skip=True
          else: num+=10
        else: num+=10
      elif s[i] =='I':
        if i+1 <n : 
          if s[i+1] == 'V': 
            num +=4
            skip=True
            #print('-',num)
          elif s[i+1] == 'X': 
            num +=9
            skip=True
          else: num+=1
        else: num+=1
      elif s[i] =='V': num+=5
      elif s[i] =='L': num+=50
      elif s[i] =='D': num+=500
    #print(num)
    return num

