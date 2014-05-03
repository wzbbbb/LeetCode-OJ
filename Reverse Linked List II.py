# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
  def reverseBetween(self, head, m, n):
    if m==n: return  head
    dummy=ListNode(0)
    dummy.next=head
    if m==1: ppm=dummy # pm , pn point to mth, and nth node,ppm, ppn, the nodes before
    cnt=0 ; node=dummy
    while cnt<m-1:
      cnt+=1
      node=node.next
    ppm=node ;pm=ppm.next; cnt=0 ; node=dummy
    while cnt<n:
      cnt+=1
      node=node.next
    pn=node
    while ppm.next!=pn:
      #print ppm.val, pm.val, pn.val
      tmp=ppm.next
      ppm.next=pm.next
      pm.next=pm.next.next
      ppm.next.next=tmp
    return dummy.next       

