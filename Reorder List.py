# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
  def reorderList(self, head): # in-place, and put in an array 
    sto,n=[],head
    while n: 
      sto.append(n)
      n=n.next
    leng,i=len(sto),0 
    if leng%2==0:
      while i < leng //2 -1:
        sto[i].next=sto[leng-1-i]
        sto[leng-1-i].next=sto[i+1]
        sto[leng-1-i-1].next=None
        i+=1
    else:
      while i < leng //2 :
        #print sto[i].val
        sto[i].next=sto[leng-1-i]
        sto[leng-1-i].next=sto[i+1]
        sto[leng-1-i-1].next=None
        i+=1
    return head

