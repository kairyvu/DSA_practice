class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        inDegree = [0] * numCourses
        for c, p in prerequisites:
            adj[p].append(c)
            inDegree[c] += 1
        
        q = deque()

        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        
        res = []

        while q:
            course = q.popleft()
            res.append(course)
            
            for nextCourse in adj[course]:
                inDegree[nextCourse] -= 1
                if inDegree[nextCourse] == 0:
                    q.append(nextCourse)
        return res if len(res) == numCourses else []