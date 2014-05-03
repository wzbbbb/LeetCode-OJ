# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
  def deleteDuplicates(self, head):
      if not head or not head.next: return head
      n=head
      while n:
        if n.next: 
          if n.next.val==n.val:
            n.next=n.next.next
          else:n=n.next
        else: n=n.next
      return head      

