class TimeMap:

    def __init__(self):
        self.state = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.state[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.state:
            return ""
        
        l, r = 0, len(self.state[key]) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2

            if timestamp == self.state[key][mid][1]:
                return self.state[key][mid][0]

            elif timestamp < self.state[key][mid][1]:
                r = mid - 1

            else:
                res = self.state[key][mid][0]
                l = mid + 1
        
        return res
