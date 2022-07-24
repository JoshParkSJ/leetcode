# O(v + e) time | O(v) space
# Union find
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]   # leads to my parent's node val 
        rank = [1] * n                    # num of nodes connected to me 
        
        def find(node):            
            while node != parents[node]:
                # path compression 1->2->3 to 1->2<-3
                parents[node] = parents[parents[node]] 
                node = parents[node]
            return node
    
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            
            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                parents[p2] = p1
                rank[p1] += rank[p2]
            else:
                parents[p1] = p2
                rank[p2] += rank[p1]
            return 1
        
        result = n
        for n1, n2 in edges:
            result -= union(n1,n2)
        return result

# --------------------------------------------------------------------------------

def buildAdjacencyList(self, n, edges):
	adjList = [[] for _ in range(n)]
	for v1, v2 in edges:
		adjList[v1].append(v2)
		adjList[v2].append(v1)
	return adjList


# DFS
class Solution:            
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
    	# in order for a graph to be a tree it must be acylic, connected, and e = n-1
		if n - 1 != len(edges):
            return False

        adjList = self.buildAdjacencyList(n, edges)
        visited = set()
        
        def hasCycle(v, parent):
            visited.add(v)

            for neighbor in adjList[v]:
                if neighbor not in visited:
                    if hasCycle(neighbor, v):
                        return True
                elif neighbor != parent:
                    return True
            
            return False
        
		# we only search with one vertex. This helps to check if the graph is connected in the next step.
        if hasCycle(0, -1):
            return False
        
		# If the graph is connected then all vertices must be visited
        return True if len(visited) == n else False

	def countComponents(n, edges):
	        def dfs(n, g, visited):
	            if visited[n]:
	                return
	            visited[n] = 1
	            for x in g[n]:
	                dfs(x, g, visited)
	                
	        visited = [0] * n
	        g = {x:[] for x in xrange(n)}
	        for x, y in edges:
	            g[x].append(y)
	            g[y].append(x)
	            
	        ret = 0
	        for i in xrange(n):
	            if not visited[i]:
	                dfs(i, g, visited)
	                ret += 1
	                
	        return ret

# --------------------------------------------------------------------------------------------
# BFS
class Solution:
	def validTree(self, n: int, edges: List[List[int]]) -> bool:
		# in order for a graph to be a tree it must be acylic, connected, and e = n-1
		if n - 1 != len(edges):
            return False
			
        adjList = self.buildAdjacencyList(n, edges)
        visited = set()
        queue = [0]
        parent = [-1] * n
        
        while queue:
            v = queue.pop(0)      
            visited.add(v)
            for neighbor in adjList[v]:
                if neighbor not in visited:
                    parent[neighbor] = v
                    queue.append(neighbor)
                elif neighbor != parent[v]:
                    return False

		 # If the graph is connected then all vertices must be visited
        return len(visited) == n

	def countComponents(n, edges):
	        g = {x:[] for x in xrange(n)}
	        for x, y in edges:
	            g[x].append(y)
	            g[y].append(x)
	            
	        ret = 0
	        for i in xrange(n):
	            queue = [i]
	            ret += 1 if i in g else 0
	            for j in queue:
	                if j in g:
	                    queue += g[j]
	                    del g[j]

	        return ret
