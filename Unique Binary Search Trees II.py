# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
  def generateTrees(self, n):
    if n==0: return self.leaf2root(1,0)
    else: return self.leaf2root(1,n)

  def leaf2root(self, st,en): # split the range to left and right part, and link the node buttom up.
    subtree=[]                # does not need to be a parameter, only used in the back trace, 
    if st > en:               # automatically become [] after each retrace
      subtree.append(None)
      return subtree 
    for i in range(st,en+1):  # like a regular loop to add one left and 1 right node
      lftree=self.leaf2root(st,i-1)
      rttree=self.leaf2root(i+1,en)
      m=len(lftree)              # reached the last 2 numbers in the left and right ranges
      q=len(rttree)
      for j in range(m): 
        for k in range(q):
          node=TreeNode(i)  # each time create a new node for i, so for each possible left node or right node 
          node.left=lftree[j]   # there is a new node i and save it as root. at the end all the roots saved.
          node.right=rttree[k]
          subtree.append(node)
    return subtree

