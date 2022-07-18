# DFS with 3 states
# O(v+e) time | O(v+e) space for adj list
class Solution:
    def buildAdjacencyList(self, n, edgesList):
        adjList = [[] for _ in range(n)] # can't do [[] * n]
        for c1, c2 in edgesList:
            adjList[c2].append(c1) # remember we're appending!
        return adjList

        # we prefer adj list over edj list because edj list needs O(len(edgelist)) to get all descendants of a given vertex
        # edj list has [ [v3, v1], ...]   where v1 -> v3 
        # adj list has { v1: [v3], ... } where v1 -> v3  
        # prereq -> course, we want to start from pre-req and after checking off pre-reqs start checking courses

        # assumption we're making: numCourses and course numbering is 0,1,2,3,4..
        # if the course numbering was in string:
        #   - state: instead of an array, use dictionary
        #   - iterating through vertex: iterate through dictionary

		
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = self.buildAdjacencyList(numCourses, prerequisites)

        # -1: is processing
        # 0: not visited
        # 1: visited
        state = [0] * numCourses # len of numCourses, NOT prerequesites (i.e # of vertices not # of edges)

        def hasCycle(v):
            if state[v] == 1:
                # This vertex is processed so we pass.
                return False
            if state[v] == -1:
                # This vertex is being processed and it means we have a cycle.
                return True

            # Set state to -1
            state[v] = -1

            for i in adjList[v]:
                if hasCycle(i):
                    return True

            state[v] = 1
            return False

        # we traverse each vertex using DFS, if we find a cycle, stop and return
        for v in range(numCourses):
            if hasCycle(v):
                return False

        return True

# ---------------------
# DFS with set
# O(v+e) time | O(v+e) space
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build Adjacency list from Edges list
        adjList = self.buildAdjacencyList(numCourses, prerequisites)
        visited = set()

        def hasCycle(v, stack):
            if v in visited:
                if v in stack:
                    # This vertex is being processed and it means we have a cycle.
                    return True
                # This vertex is processed so we pass
                return False

            # mark this vertex as visited
            visited.add(v)
            # add it to the current stack
            stack.append(v)

            for i in adjList[v]:
                if hasCycle(i, stack):
                    return True

            # once processed, we pop it out of the stack
            stack.pop()
            return False

        # we traverse each vertex using DFS, if we find a cycle, stop and return
        for v in range(numCourses):
            if hasCycle(v, []):
                return False

        return True


# --------------------
# BFS Topological sort: put all vertices horizontally on a line, all of the edges are pointing from left to right (if a cycle exists, this is impossible)
# idea: start with courses with no pre-reqs. For every descendant of course with no pre-req, make the descendants a course with no pre-req
class Solution:
    def topoBFS(self, numNodes, edgesList):
        adjList = self.buildAdjacencyList(numNodes, edgesList)

        # A list stores number of incoming edges of each vertex
        inDegrees = [0] * numNodes
        for v1, v2 in edgesList:
            inDegrees[v1] += 1 # v1 has +1 vertext pointing to it (v1 <- v2)

        # A queue of all vertices with no incoming edge
        # at least one such node must exist in a non-empty acyclic graph
        # vertices in this queue have the same order as the eventual topological sort
        queue = deque([])
        for v in range(numNodes):
            if inDegrees[v] == 0:
                queue.append(v)
        
        count = 0 # initialize count of visited vertices
        topoOrder = [] # optional, an empty list that will contain the final topological order

        while queue:
            v = queue.popleft()
            topoOrder.append(v) # optional
            count += 1

            # inDegrees and adjList are complements
            # adjList[v] = des    means v ---> des
            # inDegrees[des] -= 1 means v -x-> des
            for des in adjList[v]:
                inDegrees[des] -= 1

                if inDegrees[des] == 0: # des does not have any prereqs (i.e may have stuff pointing to it, but des does not point to anything)
                    queue.append(des)

        if count != numNodes:
            return False  # graph has at least one cycle
        else:
            return True # topOrder is a topologically sorted graph

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return self.topoBFS(numCourses, prerequisites)


