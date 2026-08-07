from collections import defaultdict, deque
from typing import List

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)
        indegree = [0] * (n + 1)

        for pre, nxt in relations:
            graph[pre].append(nxt)
            indegree[nxt] += 1

        def bfs():
            q = deque()

            for c in range(1, n + 1):
                if indegree[c] == 0:
                    q.append(c)

            sems = 0
            taken = 0

            while q:
                sems += 1

                for _ in range(len(q)):
                    course = q.popleft()
                    taken += 1

                    for nxt in graph[course]:
                        indegree[nxt] -= 1

                        if indegree[nxt] == 0:
                            q.append(nxt)

            return sems if taken == n else -1

        return bfs()