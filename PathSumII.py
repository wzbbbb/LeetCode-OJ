# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    #def pathSum(self, root, sum):
  def pathSum(self, n,summ,res=None, path=None,tmp=None):
    if res is None: res=0; path=[] ; tmp=[] 
    if n:
      res+=n.val
      tmp.append(n.val)
      if n.left is None and n.right is None and res==summ: # a leaf
        path.append(tmp[::])
        tmp.pop()
        return path
      path=self.pathSum(n.left, summ, res, path,tmp)
      path=self.pathSum(n.right, summ, res, path,tmp)
      tmp.pop()
    return path
