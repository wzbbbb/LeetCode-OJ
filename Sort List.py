# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    #def sortList(self, head):
  def split(self,n): # return 2 linked list heads
    if n.next==None: return n, None
    if n.next.next==None: 
      h2=n.next
      n.next=None
      return n, h2
    fast=n.next; slow=n
    while fast and fast.next:
      slow=slow.next
      fast=fast.next.next
    h2=slow.next ; slow.next=None
    return n, h2
  def sortList(self, head):
    if not head: return  None   
    if head.next==None: return head
    lft,rgt=self.split(head)
    #self.pl(lft)
    #self.pl(rgt)
    lft=self.sortList(lft)
    rgt=self.sortList(rgt)
    res=ListNode(0)
    cur=res
    while lft and rgt:
      if lft.val < rgt.val: cur.next=lft; lft=lft.next; cur=cur.next; cur.next=None
      else: cur.next=rgt; rgt=rgt.next; cur=cur.next; cur.next=None

    if lft: cur.next=lft 
    elif rgt: cur.next=rgt
    return res.next    

