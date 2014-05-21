# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
  def isValidBST(self, root):
    A=self.trav(root)
    for i in range(1,len(A)):
      if A[i] <= A[i-1]: return False
    return True
      
  def trav(self, n,A=None):
    if A is None: A=[]
    if n:
      A=self.trav(n.left,A)
      A.append(n.val)
      A=self.trav(n.right,A)
    return A

