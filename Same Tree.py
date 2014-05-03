# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
  def isSameTree(self, p, q):
    root1=p
    root2=q
    ri1,rp1=self.trav(root1,[],[])
    ri2,rp2=self.trav(root2,[],[])
    if ri1 == ri2 and rp1==rp2: return True
    else: return False
          
  # if both pre-order and inorder are the same, then it is the same tree
  def trav(self,n,resi=[],resp=[]):
    if n:
      resi.append(n.val)
      self.trav(n.left,resi,resp)
      resp.append(n.val)
      self.trav(n.right, resi,resp)
    else: 
      resp.append('#')
      resi.append('#')
    return resi, resp

