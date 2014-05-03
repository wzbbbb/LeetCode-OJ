# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
  def mergeKLists(self, lists):
    k=len(lists)
    que,head,curr=[],None,None
    for i in range(k): # first batch in queue
      if lists[i] !=None:
        que.append((lists[i],i))
        lists[i]=lists[i].next
    while len(que) > 0:
      que1=sorted(que,key=lambda x: x[0].val, reverse=True)
      #for q in que1:
      #  print '--in que',q[0].val
      node,lis=que1.pop() 
      #print node.val, lis
      if head==None: head= node; curr=node
      else: curr.next=node; curr=node
      if lists[lis] !=None:
        que1.append((lists[lis],lis))
        lists[lis]=lists[lis].next
      que=que1[::]
    return head

