class Solution:
    # @return a boolean
  def isValid(self, s):
    stack=[]
    n=len(s)
    for i in range(n):
      if   s[i]=='(':  stack.append(s[i])
      elif s[i]=='{':  stack.append(s[i])
      elif s[i]=='[':  stack.append(s[i])
      elif s[i]==')' and len(stack)>0:  
        if stack[-1]=='(': stack.pop()
        else: return False
      elif s[i]=='}' and len(stack)>0: 
        if stack[-1]=='{': stack.pop()
        else: return False
      elif s[i]==']' and len(stack)>0:  
        if stack[-1]=='[': stack.pop()
        else: return False
      else: return False
    if len(stack) != 0: return False
    else: return True

