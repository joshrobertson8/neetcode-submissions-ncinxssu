class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        nums.sort()

        for i in range(len(nums)):

            # precheck duplicate values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            a = nums[i]
            l, r = i + 1, len(nums) - 1

            while l < r:
                total = a + nums[l] + nums[r]
                
                if total > 0:
                    r -= 1

                elif total < 0:
                    l += 1

                else:
                    res.append([a, nums[l], nums[r]])              
                    l += 1
                    r -= 1
                    
                    # check if the left side val is a duplciate
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # check if the right side val is a duplciate
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res