class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Count how many 0s, 1s, and 2s appear
        freqMap = defaultdict(int)
        for n in nums:
            freqMap[n] += 1

        # write_idx = current position in nums where we should start writing
        write_idx = 0

        # Go through the 3 possible values in sorted order
        for color in range(3):
            # Write this color freqMap[color] times
            for _ in range(freqMap[color]):
                nums[write_idx] = color
                write_idx += 1
        return nums