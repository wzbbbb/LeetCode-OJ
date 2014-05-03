# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
      if  not head : return False
      if not head.next: return False
      if not head.next.next: return False
      slow=head.next
      fast=head.next.next
      while slow!=fast :
          slow=slow.next
          if fast.next==None or fast.next.next==None: return False
          fast=fast.next.next
      return True

