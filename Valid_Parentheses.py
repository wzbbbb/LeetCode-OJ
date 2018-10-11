#s = '({}[){{[[])]}})'
s = '[{](})'

def validate(s):
  stack = []
  if len(s) % 2 != 0 : return False
  for s1 in s:
    if s1 == '(' or s1 == '[' or s1 =='{':
      stack.append(s1)
    else:
      b = stack.pop()   #<- this is wrong form input ']'
      if (b == '(' and s1 != ')') or (b == '[' and s1 != ']')  or ( b =='{' and s1 != '}'):
        return False
  return True

print validate(s)
# Submission Result: Accepted 83.16%
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        if len(s) % 2 != 0:
            return False
        stack = ''
        for s1 in s:
            if s1 == '(' or s1 == '{' or s1 == '[':
                stack += s1
            elif len(stack) >0:
                if s1 == ')' and stack[-1] == '(':
                    stack = stack[:-1]
                elif s1 == ']' and stack[-1] == '[':
                    stack = stack[:-1]
                elif s1 == '}' and stack[-1] == '{':
                    stack = stack[:-1]
                else: return False
            else: 
                return False
        return len(stack) == 0
