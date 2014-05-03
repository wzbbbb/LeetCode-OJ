# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
  def insert(self, intervals, newInterval):
    ts=[]
    ts.append(('s',newInterval.start))
    ts.append(('e',newInterval.end))
    for a in intervals:  #attach start and end times into a list
      ts.append(('s',a.start))
      ts.append(('e',a.end))
    tss=sorted(ts,key=lambda x:x[1]) #sort the list by time
    cnt=0
    res=[]
    n=len(tss)
    for i in range(n): # if the start and end at the same time, make sure the start count first. 
      if i+1<n:
        if tss[i][1] == tss[i+1][1] and tss[i][0] =='e'and tss[i+1][0]=='s':
          tss[i],tss[i+1]= tss[i+1], tss[i]
    startp,endp=None,None
    for t in tss:  # if the cnt ==0, interval end
      if t[0]=='s' :
        if cnt==0: startp=t[1]
        cnt+=1
      elif t[0] =='e' :
        if cnt==1: endp=t[1]
        cnt-=1 
      if startp!=None and endp!=None:
        a=Interval(startp,endp)
        res.append(a)
        startp=None; endp=None
    return res

