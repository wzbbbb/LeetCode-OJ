# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    #def inorderTraversal(self, root):
  def inorderTraversal(self, root,res=None):
    if res is None: res=[]
    if root:
      res=self.inorderTraversal(root.left,res)
      res.append( root.val)
      res=self.inorderTraversal(root.right,res)
    return res
