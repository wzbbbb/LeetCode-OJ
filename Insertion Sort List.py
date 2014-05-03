# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
  def insertionSortList(self, head):
    A=[]
    if not head: return head
    A.append(head)
    n=head.next
    m=1
    while n:
      i=m-1
      inserted=False
      while i>= 0:
        if n.val > A[i].val :
          #print 'insert', n.val ,'at',i
          A.insert(i+1,n) ; inserted=True; break
        i-=1
      if inserted==False: 
        A.reverse()
        A.append(n)
        A.reverse()
      n=n.next
      m+=1
    for i in range(len(A)-1):
      A[i].next=A[i+1]
    A[-1].next=None
    return A[0]      

