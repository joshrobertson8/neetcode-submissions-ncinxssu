from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)

        for nxt, pre in prerequisites:
            graph[pre].append(nxt)

        state = [0] * numCourses

        # 0: new
        # 1: currently visiting
        # 2: safe

        def dfs(course) -> bool:

            if state[course] == 2:
                return True

            if state[course] == 1:
                return False

            state[course] = 1

            for c in graph[course]:
                if not dfs(c):
                    return False

            state[course] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True