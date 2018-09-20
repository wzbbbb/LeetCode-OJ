'''["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
  This is a stack operation. For example, 4,13,5,/ -> pop off 13/5 -> push in 4, (13/15), +
'''
#A = ["4", "13", "5", "/", "+"]
A = ["2", "1", "+", "3", "*"]
def polish(A):
  stack=[]
  S=set(['+', '-', '*', '/'])
  for a in A:
    if a in S:
      oper2=stack.pop()
      oper1=stack.pop()
      if a == '+':
        stack.append(oper1 + oper2)
      if a == '-':
        stack.append(oper1 - oper2)
      if a == '*':
        stack.append(oper1 * oper2)
      if a == '/':
        stack.append(oper1 / oper2)
    else:
      stack.append(int(a))
  return stack.pop()
print polish(A)
