class Solution:
    # @param prices, a list of integer
    # @return an integer
  def maxProfit(self, prices):
      A=prices
      profit =0
      n=len(A)
      hold=0
      buy,sell=[],[]
      for i in range(n):
        if i +1 < n and A[i] < A[i+1] and hold==0:
          hold =1
          buy.append(A[i])
        elif i +1 < n and hold==1 and A[i] >A[i+1]:
          hold=0
          sell.append(A[i])
        elif i +1 ==n and A[i] >A[i-1]:
          hold=0
          sell.append(A[i])
        #print buy, sell
      if len(sell)< len(buy): sell.append(A[-1])

      for i in range(len(buy)):
        profit+=sell[i] -buy[i]
      return profit

