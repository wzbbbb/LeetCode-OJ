# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
  #def minDepth(self, root):
  def minDepth(self, root,cnt=None,depth=0):
    #dfs
    if root:
      if cnt is None: cnt=1; depth=1
      if root.left is None and root.right is None:
        #print root.val , depth
        if depth==1: depth=cnt
        elif cnt < depth: depth=cnt 
      depth=self.minDepth(root.left,cnt+1, depth)
      depth=self.minDepth(root.right,cnt+1, depth)
    if cnt is not None: cnt-=1
    return depth
