class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = collections.deque()
        self.value = value
        self.k = k
        self.count = 0
        
    def consec(self, num: int) -> bool:
        if self.k == len(self.stream):
            if self.stream[0] == self.value:
                self.count -= 1
            self.stream.popleft()
        self.stream.append(num)
        if num == self.value:
            self.count += 1
        return self.count == self.k
        

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)