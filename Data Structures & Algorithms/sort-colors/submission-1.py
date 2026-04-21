class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        freqMap = defaultdict(int)
        for n in nums:
            freqMap[n] += 1

        write_idx = 0

        # {1 : 2, 0 : 1, 2 : 1}
        
        for color in range(3):
            for i in range(freqMap[color]):
                nums[write_idx] = color
                write_idx += 1

        return nums