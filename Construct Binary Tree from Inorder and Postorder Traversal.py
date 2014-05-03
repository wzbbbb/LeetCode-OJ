# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    #def buildTree(self, inorder, postorder):
  def buildTree(self, inorder, postorder,root=None,parent=None,side=None):
    if len(postorder)==0: return root                                      
    #print 'inorder---', inorder
    num=postorder.pop()
    #print '--num',num, postorder
    node=TreeNode(num)
    if root==None:
      root=node
    else:
      if side=='lf': parent.left=node
      elif side=='rt': parent.right=node
    idx=inorder.index(num)
    i_lft=inorder[:idx]          
    i_rgt=inorder[idx+1:]
    #postorder has the same length. the root in on the right side at the end. 
    # preorder, root on the left sice at the beginning.
    p_lft= postorder[:idx]
    p_rgt= postorder[idx:]
    #print 'lft',i_lft,p_lft,'rgt',i_rgt, p_rgt
    root=self.buildTree(i_lft,p_lft,root,node,'lf')
    root=self.buildTree(i_rgt,p_rgt,root,node,'rt')
    return root
   

