#s = '({}[){{[[])]}})'
s = '[{](})'

def validate(s):
  stack = []
  if len(s) % 2 != 0 : return False
  for s1 in s:
    if s1 == '(' or s1 == '[' or s1 =='{':
      stack.append(s1)
    else:
      b = stack.pop()
      if (b == '(' and s1 != ')') or (b == '[' and s1 != ']')  or ( b =='{' and s1 != '}'):
        return False
  return True

print validate(s)
