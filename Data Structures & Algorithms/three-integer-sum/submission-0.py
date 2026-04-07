class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        nums.sort()

        for i in range(len(nums)):
            a = nums[i]

            l, r = i + 1, len(nums) - 1

            while l < r:
                if a + nums[l] + nums[r] > 0:
                    r -= 1

                elif a + nums[l] + nums[r] < 0:
                    l += 1

                else:
                    if [a, nums[l], nums[r]] not in res:
                        res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
        return res