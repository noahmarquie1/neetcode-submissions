class StockSpanner:

    def __init__(self):
        self.counter = 0
        self.peaks: list[tuple[int]] = []
        

    def next(self, price: int) -> int:
        self.counter += 1
        span = 0

        if len(self.peaks) == 0:
            span = self.counter
        else:
            # Existing peaks, need to test when span is broken
            done = False
            while not done:
                if len(self.peaks) == 0: 
                    span = self.counter
                    done = True
                elif price < self.peaks[-1][0]:
                    span = self.counter - self.peaks[-1][1]
                    done = True
                else:
                    self.peaks.pop()

        self.peaks.append((price, self.counter))
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)