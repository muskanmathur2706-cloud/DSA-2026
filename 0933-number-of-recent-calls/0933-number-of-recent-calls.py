class RecentCounter:

    def __init__(self):
        self.requests = []
        self.start_idx = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)

        while self.requests[self.start_idx] < t - 3000:
            self.start_idx += 1
        return len(self.requests) - self.start_idx
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)