# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
  def mergeTwoLists(self, l1, l2):
    if l1==None and l2!=None: return l2
    elif l2==None: return l1
    head=l1
    n1=l1
    pn1=None
    n2=l2
    while n1 and n2:
      if n1.val > n2.val:
        if pn1==None: 
          head=n2
          n2=n2.next
          head.next=n1
          pn1=head
        else:
          pn1.next=n2
          n2=n2.next
          pn1.next.next=n1
          pn1=pn1.next
      else: 
        pn1=n1
        n1=n1.next
    if n1==None and n2!=None: pn1.next=n2 
    return head

