class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []

        counts = Counter(nums)

        countTable = sorted(counts.items(), key=lambda x: x[1], reverse=True) 

        for num, freq in countTable: 
            if k > 0:
                res.append(num)

            k -= 1

        return res  
