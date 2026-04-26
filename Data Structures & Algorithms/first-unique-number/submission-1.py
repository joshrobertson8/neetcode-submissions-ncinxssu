class FirstUnique:

    def __init__(self, nums: List[int]):
        self.freqMap = Counter(nums)
        self.q = deque(nums)

    def showFirstUnique(self) -> int:
        while self.q and self.freqMap[self.q[0]] != 1:
            self.q.popleft()

        if self.q:
            return self.q[0]
        return -1
        

    def add(self, value: int) -> None:
        self.freqMap[value] += 1
        self.q.append(value)



# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
