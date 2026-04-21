class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqMap = Counter(nums)
        res = []
        
        
        reverseMap = sorted(freqMap.items(), key=lambda x: x[1], reverse=True)


        for key, v in reverseMap:

            if k > 0:
                res.append(key)
            k -= 1
        return res