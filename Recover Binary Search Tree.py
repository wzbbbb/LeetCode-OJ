# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
  def recoverTree(self, root):
    self.swapr(root)
    self.swapl(root)
    return root
  def swapr(self, n,pn=None):
    if n:
      pn=self.swapr(n.left,pn)
      if pn==None: pn=n
      elif n.val < pn.val :
        n.val,pn.val=pn.val,n.val
      pn=n
      pn=self.swapr(n.right,pn)
    return pn
  def swapl(self, n,pn=None):
    if n:
      pn=self.swapl(n.right,pn)
      if pn==None: pn=n
      elif n.val > pn.val :
        n.val,pn.val=pn.val,n.val
      pn=n
      pn=self.swapl(n.left,pn)
    return pn      

