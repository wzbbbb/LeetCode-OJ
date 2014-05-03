# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    #def levelOrderBottom(self, root):
  def levelOrderBottom(self, root):  # the bfs way
    if not root: return []
    que,res,lvl=[],[],0
    n=root
    res.append([n.val])
    while n:
      if n.left: que.append((n.left,lvl+1))
      if n.right: que.append((n.right,lvl+1))
      if len(que)>0:
        que.reverse()
        n,lvl=que.pop()
        que.reverse()
        if lvl >=len(res): res.append([n.val])
        else: res[-1] += [n.val]
      else: n=None
    out=[]
    for i in range(len(res)-1,-1,-1):
      out.append(res[i])
    return out

