class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        bank  = set(nums)
        globalMax = 0

        for num in bank:

            if num - 1 not in bank:
                curMax = 0

                while num + curMax in bank:
                    curMax += 1

                globalMax = max(globalMax, curMax)

        return globalMax