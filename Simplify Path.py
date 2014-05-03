class Solution:
    # @param path, a string
    # @return a string
  def simplifyPath(self, path):
    A=[]
    B=[]
    A=path.split('/')
    for a in A:
      #print('--',a)
      #print(B)
      if a=='..' and len(B)>0: B.pop()
      elif a!='.' and a!='..' and a!='': B.append(a)
      else:
        if len(a) >1 and a[0] =='.' :
          if a[1] !=a[0]: B.append(a[1:])
          elif a[1] !=a[0]: B.append(a) 
    #print(B)
    output=''
    for b in B:
      output+='/'+b
    #print('output',output)
    if output=='': return '/'
    return output

