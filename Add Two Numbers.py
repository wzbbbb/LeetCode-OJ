# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @return a ListNode
  def addTwoNumbers(self, l1, l2):
    num1=self.read_ll(l1)
    num2=self.read_ll(l2)
    num=num1+num2
    return self.build_ll(num)
  def read_ll(self,n):
    res,base=[],10
    while n:
      res.append(n.val)
      n=n.next
    n=len(res)
    out=0
    for i in range(n-1,-1,-1):
      out=out* base+res[i] 
    return out
  def build_ll(self,num):
    dummy=ListNode(0); pre=dummy
    if num==0: 
      root=ListNode(0)
      return root
    while num >0:
      c=num%10
      node=ListNode(c)
      #node.next=dummy.next
      pre.next=node
      pre=node
      num=num//10
    return dummy.next

