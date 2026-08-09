from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)

        for nxt, pre in prerequisites:
            graph[pre].append(nxt)

        path = set()   # nodes currently in DFS path
        safe = set()   # nodes already fully checked

        def dfs(course) -> bool:

            if course in path:
                return False

            if course in safe:
                return True

            path.add(course)

            for nxt in graph[course]:
                if not dfs(nxt):
                    return False

            path.remove(course)
            safe.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True