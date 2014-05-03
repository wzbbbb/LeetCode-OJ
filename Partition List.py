# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
  def partition(self, head, x):
      if not head or not head.next: return head
      n=head
      root=ListNode(0)
      root.next=n
      bl=root #the last small node , point to ln
      ln=root # the first big node
      pre=root
      while n:
        #print  'bl',bl.val,'ln',ln.val, 'pre:',pre.val,'n', n.val,'n.next', n.next.val
        if n.val>=x and ln==root : # first big element
          bl=pre
          pre=n
          ln=n
          n=n.next
        elif n.val <x and ln!=root:
          bl.next=n
          pre.next =n.next
          n.next=ln
          bl=n
          n=pre.next
          #print '--bl',bl.val,'ln',ln.val, 'pre:',pre.val,'n', n.val,'n.next', n.next.val
          #print_ll(n1)
        else:
          pre=n
          n=n.next
      return root.next      

