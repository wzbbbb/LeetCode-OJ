# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
  def maxPoints(self, points):
    # loop through all points, to find all slops to them from the current point
    # for duplicate points, add each to the max number
    n=len(points)
    if n<=2: return n
    pts=sorted(points, key=lambda x: x.x)
    #slops=[]
    maxp=[1 for i in range(n)]
    for i in range(n): 
      if i>0: 
        if pts[i].x==pts[i-1].x and pts[i].y==pts[i-1].y: continue
      dup=0; slops=dict()
      for j in range(i+1,n):
        x1=pts[i].x; y1=pts[i].y; x2=pts[j].x; y2=pts[j].y
        #print x1,y1,x2,y2
        if x1==x2 and y1==y2: dup+=1
        elif x1==x2 and y1!=y2: 
          if None in slops.keys(): slops[None] +=1
          else: slops[None] =1
        elif x1!=x2 : 
          sl=(y1-y2)/(x1-x2*1.0) 
          if sl in slops.keys(): slops[sl] +=1
          else: slops[sl] =1
      #print slops
      if len(slops)>0:
        maxp[i]=max(slops.values())+1
      if  dup >0: maxp[i]+= dup
      #print 'maxp',maxp
    return  max(maxp)

