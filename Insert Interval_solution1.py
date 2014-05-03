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
    newi=newInterval
    inv=intervals
    ind=None
    if len(inv)==0: return [newi]
    inv.append(newi)
    res=self.merge(inv)
    return res
  def merge(self, intervals):
    n=len(intervals)
    ivs=sorted(intervals, key=lambda x: x.start)
    to_rm=[]
    i=0
    while i < n:
      if i+1<n:
        if ivs[i].end -ivs[i].start >=ivs[i+1].end-ivs[i+1].start: 
          if ivs[i+1].start <= ivs[i]. end : # start included
            if ivs[i+1].end>ivs[i].end : # end not included 
              ivs[i].end=ivs[i+1].end
            ivs.pop(i+1)
            n=len(ivs)
          else: i +=1
        elif ivs[i].end-ivs[i].start  <ivs[i+1].end-ivs[i+1].start: 
          if ivs[i].end >= ivs[i+1].start : # end included
            if ivs[i].start < ivs[i+1].start: # start not included
              ivs[i+1].start=ivs[i].start
            ivs.pop(i)
            n=len(ivs)
          else: i +=1
      else: i+=1
    return  ivs

