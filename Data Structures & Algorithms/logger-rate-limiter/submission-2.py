class Logger:

    def __init__(self):
        self.constraint_window = 10
        self.timestamp_map = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # check if the message is in timestamp_map
        prev = self.get_timestamp(message)
        if prev < 0 or self.is_timestamp_valid(prev, timestamp):
            self.timestamp_map[message] = timestamp
            return True

        return False
    
    def get_timestamp(self, message: str) -> int:
        return self.timestamp_map.get(message, -1)
    
    def is_timestamp_valid(self, prev: int, curr: int) -> bool:
        return (curr - prev) >= self.constraint_window


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
