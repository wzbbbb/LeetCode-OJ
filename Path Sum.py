# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    #def hasPathSum(self, root, sum):
  def hasPathSum(self, n,summ,res=0, out=False,path=[]):
    if n:
      res+=n.val
      #path.append(n.val)
      #print res, n.val
      if n.left==None and n.right==None and res==summ : # leaf
        out=True
        #print path, res, out
        return out
        #return res, out
      out=self.hasPathSum(n.left,summ, res,out,path)
      out=self.hasPathSum(n.right,summ, res,out,path)
      #print path
      #path.pop()
    return  out    

