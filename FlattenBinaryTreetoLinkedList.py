# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
  def flatten(self, root):
    # keep all node in a list, then remove left and add to right in sequence
    order=self.walk(root)
    n=len(order)
    for i in range(1,n):
      order[i-1].left=None
      order[i-1].right=order[i]

  def walk(self,n,order=None):
    if order is None: order=[]
    if n:
      order.append(n)
      order=self.walk(n.left,order)
      order=self.walk(n.right,order)
    return order
