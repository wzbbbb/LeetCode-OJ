class Solution:
    # @param s, a string
    # @return an integer
  def longestValidParentheses(self, s):
    op,cl,res,stack,cnt=[],[],0,[],0
    n=len(s)
    for i in range(n):
      if s[i] =='(':  stack.append(i)
      elif s[i] ==')' and len(stack) >0: 
        op.append(stack.pop())
        cl.append(i)
    #print op, cl
    A=sorted(op+cl)
    m=len(A)
    cnt=1
    if m==0: return 0
    elif m==1: return cnt
    elif m>1:
      for j in range(1,m):
        if A[j] -A[j-1] ==1:
          cnt+=1
        else: 
          if cnt> res: res=cnt
          cnt=1
    if cnt> res: res=cnt
    return res

