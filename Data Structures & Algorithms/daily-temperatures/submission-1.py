from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        # [temperature, index]
        stack = []

        for i in range(n):
            cur_temp = temperatures[i]

            while stack and cur_temp > stack[-1][0]:
                prev_temp, prev_index = stack.pop()
                res[prev_index] = i - prev_index

            stack.append([cur_temp, i])

        return res