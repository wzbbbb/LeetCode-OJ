# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
  def minDepth(self, root):
    #bfs, stops at the first leaf node
    if root is None: return 0 
    que=[] ; que.append((root,1))
    while que[0]:
      if que[0][0].left is None and que[0][0].right is None:
        return que[0][1]
      if que[0][0].left is not None: que.append((que[0][0].left,que[0][1]+1))
      if que[0][0].right is not None: que.append((que[0][0].right, que[0][1]+1))
      que.reverse()
      que.pop()
      que.reverse()
