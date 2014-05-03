# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    #def reverseKGroup(self, head, k):
  def reverse(self, pre, head,k):
    n,cnt=head,0
    while n:
      cnt+=1
      #print(pre.next.val)
      if cnt < k:
        tmp=pre.next
        pre.next=n.next
        n.next=n.next.next
        pre.next.next=tmp
        #n=n.next
      else: break
    n= pre.next
    #while n: 
     # print('++--',n.val)
      #n=n.next
    return pre.next
  def reverseKGroup(self, head, k):
    dummy=ListNode(0)
    dummy.next=head
    pre=dummy
    pb,m=head,head   #pb: beginning of the next cycle
    nextrun,firstrun=True, True
    while head:
      #print('--pb,m',pb.val, m.val)
      cnt=0
      while m:
        cnt+=1
        if cnt ==k: 
          nextrun=True
          break
        m=m.next
      if m: m=m.next # move to next before the next reverse
      else: break
      #print('==pb,m',pb.val, m.val)
      if nextrun: 
        #print ('calling==',pb.val,pre.val)
        if firstrun:
          head=self.reverse(pre,pb,k)
          firstrun=False
        else : dummy1=self.reverse(pre,pb,k)
        nextrun=False
        pre=pb
        pb=m
        #print('**pb,m',pb.val, m.val)
      else: break
    return head

