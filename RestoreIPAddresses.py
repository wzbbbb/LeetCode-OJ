ass Solution:
    # @param s, a string
    # @return a list of strings
    #def restoreIpAddresses(self, s):
  def restoreIpAddresses(self,s,startp=0,res=None,tmp=None):
    if res is None: res=[]; tmp=[]
    if len(tmp)>4 : return res
    elif len(tmp)==4 :
      l=0
      for t in tmp:
        if len(t)>1 and t[0]=='0':
          l=-1 # a field start with 0, to make sure the l != len(s)
        l+=len(t)
      if l ==len(s):
        IP=tmp[0] +'.'+ tmp[1]+'.'+tmp[2]+'.'+tmp[3]
        if IP not in res: res.append(IP)
      return res
    for i in range(1,4): # find all possible field up to 3 digit
      endp=startp +i
      if endp <= len(s):
        if int(s[startp:endp]) > 255: continue
        else: 
          tmp.append(s[startp:endp])
          res=self.restoreIpAddresses(s,endp,res,tmp)
          tmp.pop()
    return res
