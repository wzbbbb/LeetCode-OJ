# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
  def sortedListToBST(self, head):
    if not head: return None
    A=[]
    while head:
      A.append(head.val)
      head=head.next
    return  self.arrayToTree(A)
  def arrayToTree(self, A,root=None,parent=None,side=None):
    n=len(A)
    if n<1: return 
    node=TreeNode(A[n//2])
    lft=A[:n//2]
    rgt=A[n//2+1:]
    if parent!=None:
      if side=='lf': parent.left=node
      else: parent.right=node
    else: root=node 
    if len(lft) >=1: root=self.arrayToTree(lft,root, node,'lf')
    if len(rgt) >=1: root=self.arrayToTree(rgt,root, node,'rt')
    return root

