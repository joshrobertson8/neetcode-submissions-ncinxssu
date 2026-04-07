class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        u_nums = set(nums)

        if len(u_nums) == len(nums):
            return False
        return True