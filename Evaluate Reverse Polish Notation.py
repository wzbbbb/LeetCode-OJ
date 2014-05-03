class Solution:
    # @param tokens, a list of string
    # @return an integer
  def evalRPN(self, tokens):
    b=tokens[::]
    used=set()
    for i in range(len(b)):
        neg1,neg2=1, 1
        if b[i]=='+' :
            j=self.findnext(used,i-2)
            c=int(b[j]) + int(b[i-1])
        elif b[i]=='-' :
            j=self.findnext(used,i-2)
            c=int(b[j]) - int(b[i-1])
        elif b[i]=='*' :
            j=self.findnext(used,i-2)
            c=int(b[j]) * int(b[i-1])
        elif  b[i]=='/':
            j=self.findnext(used,i-2)
            #print b[j], '/', b[i-1]
            if int(b[j]) < 0: neg2=-1
            if int(b[i-1]) < 0: neg1=-1
            if int(b[i-1]) ==0: return None
            c=abs(int(b[j])) / abs(int(b[i-1])) * neg1*neg2
        if b[i]=='+' or b[i]=='-' or b[i]=='*' or b[i]=='/' :
            #print '--',c, b, used
            b[i]=c
            used.add(i-1)
            used.add(j)
    return int(b[-1])
  def findnext(self,used,k):
    while k in used:
      k-=1
    return k

