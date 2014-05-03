# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
  def copyRandomList(self, head):
    # map the old list to the new list with dict(),
    # when a random pointer point to a node in old, in the new list find the node with dict
    n,pn1,dic,head1=head,None,dict(),None  
    while n:                      # and build the pointer 
      #print n.label
      if pn1==None: 
        pn1=RandomListNode(n.label) 
        head1=pn1  
        dic[n]=pn1
      else:
        pn1.next=RandomListNode(n.label)
        pn1=pn1.next
        dic[n]=pn1
      n=n.next
      #print '---',n.label
    n=head
    n1=head1
    while n:
      if n.random ==None: n1.random=None
      else: n1.random=dic[n.random]
      n=n.next
      n1=n1.next
    return head1

