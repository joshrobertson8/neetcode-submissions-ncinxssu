class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Use Kadanes algorithm

        if not nums: 
            return 0
        
        maxSum = nums[0]
        curSum = 0

        for num in nums: 
            curSum = max(curSum, 0) # reset negative sums to 0 as they are hopeless
            curSum += num
            maxSum = max(maxSum, curSum)
        
        return maxSum