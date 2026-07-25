class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        ans = 0

        def backtrack(curSum, i):
            nonlocal ans
            
            if i == len(nums):
                if sum(curSum) == target:
                    ans += 1
                return
            
            currPlus = curSum.copy()
            currNeg = curSum.copy()

            
            currPlus.append(nums[i])
            currNeg.append(-nums[i])
                        
            backtrack(currPlus, i + 1)
            backtrack(currNeg, i + 1)
        
        backtrack([], 0)
        return ans