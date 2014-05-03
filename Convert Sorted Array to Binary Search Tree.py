# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    #def sortedArrayToBST(self, num):
  def sortedArrayToBST(self, num,parent=None,side=None,root=None): # use middle one as root, and left and right branch
    n=len(num)
    if n<1: return root 
    node=TreeNode(num[n//2])
    if side==None: root=node
    elif side=='lf':  parent.left=node
    elif side=='rt':  parent.right=node
    if  n== 1: return root
    else:
      lft=num[:n//2 ]
      rgt=num[n//2+1:]
      root=self.sortedArrayToBST(lft,node,'lf',root)
      root=self.sortedArrayToBST(rgt,node,'rt',root)
    return  root   

