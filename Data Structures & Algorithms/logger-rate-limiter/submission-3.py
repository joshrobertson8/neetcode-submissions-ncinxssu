class Logger:

    def __init__(self):
        self.state = defaultdict(int)
        self.limit = 10

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        if self.isTimestampValid(timestamp, message):
            self.state[message] = timestamp
            return True

        return False

    def isTimestampValid(self, timestamp: int, message: str) -> bool:
        return message not in self.state or timestamp - self.state[message] >= self.limit



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
