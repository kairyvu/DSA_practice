class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for c, p in prerequisites:
            adj[c].append(p)
        learned = set()

        def dfs(course):
            if course in learned:
                return False
            if not adj[course]:
                return True
            learned.add(course)
            for pre in adj[course]:
                if not dfs(pre):
                    return False

            learned.remove(course)
            adj[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True