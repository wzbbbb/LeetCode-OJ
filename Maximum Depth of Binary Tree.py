# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
  def maxDepth(self, root):
    if root==None: return 0
    stack,seen=[],set()
    stack.append(root)
    seen.add(None)
    cnt,max=0,None
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
        if max==None : max=cnt
        elif cnt> max: max=cnt
        #print '--',root.val, cnt, max
      stack.pop()
      cnt-=1
    return max

