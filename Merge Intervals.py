# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
  def merge(self, intervals):
    n=len(intervals)
    ivs=sorted(intervals, key=lambda x: x.start)
    to_rm=[]
    i=0
    while i < n:
      #print i,n
      if i+1<n:
        #print i+1, ivs[i+1].start
        if ivs[i].end -ivs[i].start >=ivs[i+1].end-ivs[i+1].start: 
          if ivs[i+1].start <= ivs[i]. end : # start included
            if ivs[i+1].end>ivs[i].end : # end not included 
              ivs[i].end=ivs[i+1].end
            #to_rm.append(ivs[i+1]) # if included just pop out
            ivs.pop(i+1)
            n=len(ivs)
          else: i +=1
        elif ivs[i].end-ivs[i].start  <ivs[i+1].end-ivs[i+1].start: 
          if ivs[i].end >= ivs[i+1].start : # end included
            #print '--', ivs[i].start,ivs[i].end,ivs[i+1].start, ivs[i+1].end
            if ivs[i].start < ivs[i+1].start: # start not included
              ivs[i+1].start=ivs[i].start
              #print ivs[i+1].start
            ivs.pop(i)
            n=len(ivs)
          else: i +=1
      else: i+=1
    return  ivs

