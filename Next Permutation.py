class Solution:
    # @param num, a list of integer
    # @return a list of integer
  def nextPermutation(self, num):
    n,neg=len(num),False
    for i in range(n-1,0,-1):
      if num[i] > num[i-1]: #num[i] the max num so far, num[i-1] to change
        #print num[i], num[i-1], i-1
        for j in range(n-1,i-1,-1):
            if num[j] > num[i-1]: # find the first number larger than num[i]
              #print '--',num[j], num[i-1]
              num[j], num[i-1] = num[i-1], num[j]
              #print '==',num[j], num[i-1], num
              for k in range(n-1,(n-1+i)//2, -1):
                #print '++',num[k], num[i-k+n-1]
                num[k],num[i-k+n-1] =num[i-k+n-1],num[k]
        #num[i] ,num[i-1]= num[i-1] ,num[i]
              return num
    num.reverse() # already in decending order, the maximum value, send the reverse
    return num

