# brute force would be to iterate through every node, and do a max n-ary tree depth check (https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)

# O(n) time | O(n) space
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        inBound = defaultdict(int)

        for start, destination in edges:
            adjList[start].append(destination)
            adjList[destination].append(start) # undirected
            inBound[start] = inBound.get(start, 0) + 1
            inBound[destination] = inBound.get(destination, 0) + 1

        queue = deque([])
        for node in adjList:
            if inBound[node] == 1: # leaf
                queue.append(node)

        result = [] # centroids
        while queue:
            result = []
            for i in range(len(queue)): # outer/leaf layer size
                node = queue.popleft()
                result.append(node)     # in case this is the centroid layer

                for adjNode in adjList[node]: # adjNode = innerNode
                    inBound[adjNode] -= 1
                    if inBound[adjNode] == 1:
                        queue.append(adjNode)

        return result if result else [0]
