# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
  def preorderTraversal(self, root):
    stack,res=[],[]
    while root:
      res.append(root.val)
      if root.right: stack.append(root.right)
      if root.left: stack.append(root.left)
      if len(stack)>0:root=stack.pop()
      else:root=None
    return res

