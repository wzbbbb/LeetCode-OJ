class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
  def permute(self,num):
    res=[[num[0]]]
    n=len(num)
    for i in range(1,n):
        #print 'num[i]',num[i]
        lenr,tmp=len(res),[]
        #print 'res,:', res, lenr
        for h in range(lenr-1,-1,-1):#each list in res
            #print 'res[h]',res[h]
            k=len(res[h])
            tmp.append(res[h]+[num[i]] )
            for j in range(k):
                tmp.append(res[h][:j]+[num[i]]+res[h][j:])
            #print 'tmp',tmp
        res=tmp[::]
    return res

