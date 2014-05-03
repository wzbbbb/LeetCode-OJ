class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
  def canCompleteCircuit(self, gas, cost):
    n=len(gas)
    total=0
    remain=[]
    remain_t=0
    startp=0
    for i in range(n):
        remain.append(gas[i]-cost[i]) # find the usage per stop
        total+=remain[i]  # total gas - cost , if < 0, then not possible
        remain_t+=remain[i]     # current cost from this start point.
        if remain_t>=0 and startp==0:  
            startp=i
        elif remain_t<0:    # only since solution is unique, only one start point can stay positive  
            remain_t=0
            startp=0
        #print(i,startp, remain_t)
    #print(remain, total)
    if total < 0: return -1
    else: return startp

