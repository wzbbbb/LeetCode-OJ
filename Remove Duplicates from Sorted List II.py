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
      dummy=ListNode(0)# dummy node
      pre=dummy
      pre.next=n # the node before duplicate 
      while n:
        if n.next:
          #print 'n', n.val, 'n.next', n.next.val
          if n.val==n.next.val: #duplicate start
            k=n.val
            while n.val==k: # find first node after duplicates
              n=n.next
              if n==None: break
            pre.next=n
          else: # not duplicate
            pre=n
            n=n.next
        else: 
          n=n.next
      return dummy.next      

