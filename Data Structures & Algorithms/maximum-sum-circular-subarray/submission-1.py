from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]

        curMinSum = 0
        maxMinSum = nums[0]

        totalSum = 0

        for n in nums: 
            totalSum += n

            curSum = max(curSum, 0)
            curMinSum = min(curMinSum, 0)

            curSum += n
            curMinSum += n

            maxSum = max(maxSum, curSum)
            maxMinSum = min(maxMinSum, curMinSum)
        
        return max(maxSum, totalSum - maxMinSum) if maxSum > 0 else maxSum