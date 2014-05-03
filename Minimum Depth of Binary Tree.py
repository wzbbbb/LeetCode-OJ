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
    #def minDepth(self, root,count=0,path=[],mc=0,mp=[]): # minimum depth path
    if root==None: return 0
    stack,seen=[],set()
    stack.append(root)
    seen.add(None)
    cnt,min=0,None
    while len(stack)>0:
      root=stack[-1]
      while root not in seen:
        seen.add(root)
        #print root.val
        cnt+=1
        if root.right and root.right not in seen: stack.append(root.right)
        if root.left and root.left not in seen: stack.append(root.left)
        root=stack[-1]
      if stack[-1].left==None and stack[-1].right==None: # reach leaf
        if min==None : min=cnt
        elif cnt< min: min=cnt
        #print '--',root.val, cnt, min
      stack.pop()
      cnt-=1
    return min

