# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param a ListNode
    # @return a ListNode
  def swapPairs(self, head):
      n,dummy=head,ListNode(0)
      dummy.next=head
      pre=dummy
      while n:
        #print n.val
        if n.next:
          pre.next=n.next
          n.next=pre.next.next
          pre.next.next=n
          pre=pre.next.next
          n=n.next
          #print pre.val, n.val
        else: n=n.next
      return dummy.next

