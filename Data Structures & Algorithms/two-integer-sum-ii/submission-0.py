class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        hashmap = {}
        
        for num in range(len(numbers)):
            hashmap[numbers[num]] = num

        for i in range(len(numbers)):
            complement = target - numbers[i]

            if complement in hashmap:
                return [i + 1, hashmap[complement] + 1]

        return []