# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
  def removeNthFromEnd(self, head, n):
    dummy=ListNode(0)
    dummy.next=head
    prep,nod,leng=None,head,0 # prep: the one before the one to remove 
    while nod: 			
      leng+=1
      #print(nod.val)
      if leng -n == 0 and prep==None:
        #print("here")
        prep=dummy
      elif prep!=None: 
        prep=prep.next
        #print('prep',prep.val)
      nod=nod.next
    prep.next=prep.next.next
    #print(prep.val, prep.next.val)
    return dummy.next 
  

