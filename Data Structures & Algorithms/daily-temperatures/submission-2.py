class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        if not temperatures:
            return []
        
        stack = [(temperatures[0], 0)]
        res = [0] * len(temperatures)


        for i, val in enumerate(temperatures):

            while stack and val > stack[-1][0]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((val, i))

        return res                