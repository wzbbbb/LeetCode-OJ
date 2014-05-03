# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
  def rotateRight(self, head, k):
    if head==None: return head
    stp,n=0,head
    dummy=ListNode(0)
    dummy.next=head
    pre=dummy
    if head.next!=None:
      leng=0
      while n:
        leng+=1
        n=n.next
      while k>leng: 
        k=k%leng
      if k==leng: return head
      if k==0: return head
      n=head
      while n.next: 
        stp+=1
        if stp >=k: pre=pre.next
        n=n.next
      #print stp, n.val
      n.next=dummy.next
      dummy.next=pre.next
      pre.next=None
    return dummy.next

