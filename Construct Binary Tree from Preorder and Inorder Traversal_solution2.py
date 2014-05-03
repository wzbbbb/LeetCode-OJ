# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
  #def buildTree(self, preorder, inorder):
  def buildTree(self, preorder, inorder,root=None,parent=None,side=None):
    if len(preorder) == 0: return root
    #print 'pre',preorder, 'ino',inorder
    preorder.reverse()
    num=preorder.pop()
    preorder.reverse()
    node=TreeNode(num)
    if root==None: root=node
    else: 
      if side=='lf': parent.left=node
      elif side=='rt': parent.right=node
    idx=inorder.index(num)
    i_lft=inorder[:idx]
    i_rgt=inorder[idx+1:]
    p_lft=preorder[:idx]
    p_rgt= preorder[idx:]
    #print rgt,lft
    root=self.buildTree(p_lft,i_lft,root,node,'lf')
    root=self.buildTree(p_rgt,i_rgt,root,node,'rt')
    return root

