from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)

        for nxt, pre in prerequisites:
            graph[pre].append(nxt)

        seen = set()
        safe = set()

        def dfs(course) -> bool:

            if course in seen:
                return False

            if course in safe:
                return True

            seen.add(course)

            for c in graph[course]:
                if not dfs(c):
                    return False
            
            seen.remove(course)
            safe.add(course)
            
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
                
        return True