# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
      # also using dict() to make all old node to the new nodes
      # when an old node has some neighbors, the new node will add those mappings in the new graph
      # first trav build all the new nodes and add to the dict
      # second trav add all the neighbors
      dic=dict()
      dic=self.build_node_mapping(node)
      head=self.copyG(node,dic)
      return head
    def copyG(self,node,dic,seen=set(),head=None):
      if node:
        seen.add(node)
        newn=dic[node]
        if head==None: head=newn
        for u in node.neighbors[::]:
          if u!=None:
            newn.neighbors.append(dic[u])
          else : newn.neighbors.append(None)
        for v in node.neighbors:
          if v not in seen:
            head=self.copyG(v,dic,seen,head)
      return head
    def build_node_mapping(self, node,seen=set(), dic=dict()):
      if node:
        seen.add(node)
        newn=UndirectedGraphNode(node.label)
        dic[node] = newn
        for v in node.neighbors:
          if v not in seen:
            dic=self.build_node_mapping(v,seen,dic)
      return dic

