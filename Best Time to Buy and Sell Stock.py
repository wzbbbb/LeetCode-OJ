class Solution:
    # @param prices, a list of integer
    # @return an integer
  def maxProfit(self, prices):
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

