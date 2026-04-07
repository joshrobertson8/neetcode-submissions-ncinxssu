class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hashmap and hashmap[complement] != i:
                return [hashmap[complement], i]
            
            hashmap[nums[i]] = i 

        return []