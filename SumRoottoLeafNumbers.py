# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
  def sumNumbers(self, root):
    if root is None: return 0
    res=0
    path=self.walk(root)
    #print(path)
    for p in path:
      num=0
      for a in p:
        num= num*10 + a
      res+=num
    return res
  def walk(self, n,path=None,tmp=None):
    if path is None: path=[]; tmp=[]
    if n:
      tmp.append(n.val)
      if n.left is None and n.right is None:
        path.append(tmp[::])
        tmp.pop()
        return path
      path=self.walk(n.left,path,tmp)
      path=self.walk(n.right,path,tmp)
      tmp.pop()
    return path
