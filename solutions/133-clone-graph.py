"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# n is num of nodes, m is num of edges
# O(n+m) time | O(n) worst case space or O(logn) best case
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        copy = { node: Node(node.val) }
        self.dfs(node, copy)
        return copy[node]
    
    def dfs(self, node, adjList):
        for neig in node.neighbors:
            if neig not in adjList:
                adjList[neig] = Node(neig.val)
                self.dfs(neig, adjList)
            copyNode = adjList[node]
            # originalNode.neighbour.append(newNode)
            copyNode.neighbors.append(adjList[neig])