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
    for a in intervals:
      ts.append(('s',a.start))
      ts.append(('e',a.end))
    tss=sorted(ts,key=lambda x:x[1])
    cnt=0
    res=[]
    n=len(tss)
    for i in range(n): # merge adjacent interval
      if i+1<n:
        if tss[i][1] == tss[i+1][1] and tss[i][0] =='e'and tss[i+1][0]=='s':
          tss[i],tss[i+1]= tss[i+1], tss[i]

    #print(tss)
    startp,endp=None,None
    for t in tss:
      if t[0]=='s' :
        if cnt==0: startp=t[1]
        cnt+=1
      elif t[0] =='e' :
        #print(cnt,t[0])
        if cnt==1: endp=t[1]
        cnt-=1 
      if startp!=None and endp!=None:
        a=Interval(startp,endp)
        res.append(a)
        startp=None; endp=None
        
    return res

