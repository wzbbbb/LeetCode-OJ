# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
  def postorderTraversal(self, root):
    if root==None : return []

    stack,res,seen=[],[],set()
    stack.append(root)
    seen.add(None)
    while len(stack)>0:
      root=stack[-1]
      #print root.val,res, stack
      while root.left not in seen or root.right not in seen: # reach a leaf
        if root.right and root.right not in seen: 
          stack.append(root.right)
          seen.add(root.right)
        if root.left and root.left not in seen: 
          stack.append(root.left)
          seen.add(root.left)
        root=stack[-1]
      res.append(stack.pop().val)


    return res
      

