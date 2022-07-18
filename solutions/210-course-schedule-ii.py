# O(v + e) time | O(v + e) space
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(numCourses)]
        inBoundList = [0 for _ in range(numCourses)]
        topSort = []
        count = 0
        
        for course, prereq in prerequisites:
            adjList[prereq].append(course) # prereq -> course
            inBoundList[course] += 1
        
        queue = deque([])
        for course, inBound in enumerate(inBoundList):
            if inBound == 0:
                queue.append(course)
        
        while queue:
            course = queue.popleft()
            topSort.append(course) 
            count += 1
            
            for des in adjList[course]:
                inBoundList[des] -= 1 # prereq -x-> course
                
                if inBoundList[des] == 0:
                    queue.append(des)
        
        if count != numCourses:
            return []
        return topSort