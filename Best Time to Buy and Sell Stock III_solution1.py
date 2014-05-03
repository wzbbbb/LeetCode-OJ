class Solution:
    # @param prices, a list of integer
    # @return an integer
  #def maxProfit(self, prices):
  def maxProfit1(self, prices):  # question: I
    ma,mi,profit=None,None,0
    if len(prices)<=1: return 0
    for p in prices:
      if ma==None: ma=p;mi=p
      else:
        if p>ma: 
          ma=p
          if ma-mi> profit: profit= ma -mi
        if p< mi:    # when new low comes, reset max, buy before sell
          mi=p; ma=p
    return profit

  def maxProfit(self, prices):  # call the solution of I twice. brutal force
    profit=None
    ma,mi,periods=None,0,[]
    n=len(prices)
    if n<=1: return 0
    pp=prices[0]
    for i in range(n):
      if ma==None: ma=prices[i]; mi=prices[i] ;periods.append((i,i))
      if prices[i]<pp: mi=prices[i]; ma=prices[i] ; periods.append((i,i))
      elif prices[i] >pp: ma =prices[i] ;  periods[-1]=(periods[-1][0],i)
      pp=prices[i]
    #print periods 
    rmv=[]
    m=len(periods)
    for i in range(m):
      if periods[i][0]==periods[i][1]:  rmv.append(periods[i])
    #print rmv
    for r in rmv:
      periods.remove(r)
    #print periods 
    k=len(periods)
    for i in range(k):
      j=periods[i][1]+1
      #print j
      cur=self.maxProfit1(prices[:j])
      cur+=self.maxProfit1(prices[j:])
      if profit==None: profit=cur
      elif cur> profit: profit=cur
    if profit==None: return 0
    else: return profit

