class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.freqMap = Counter(nums)

    def showFirstUnique(self) -> int:
        for num in self.nums:
            if self.freqMap[num] == 1:
                return num
        return -1

    def add(self, value: int) -> None:
        self.nums.append(value)

        self.freqMap[value] += 1



# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
