# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
  def detectCycle(self, head):
    if not head : return None
    if not head.next : return None
    if not head.next.next: return None
    fast,slow=head.next.next,head.next
    while fast !=slow: # find the meeting posint
      if not slow.next : return None
      if not fast.next: return None
      if not fast.next.next: return None
      slow=slow.next
      fast=fast.next.next
    res=head
    while res != slow: # the meeting point is where the cycle begin
      res=res.next
      slow=slow.next
    return res

