import collections

class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.running_sum = 0
        self.running_size = 0
        self.queue = collections.deque()
    
    def next(self, val):
        if self.running_size < self.size:
            self.running_sum += val
            self.queue.append(val)
            self.running_size += 1
            return self.running_sum / self.running_size
        else:
            tmp = self.queue.popleft()
            self.queue.append(val)
            self.running_sum = self.running_sum - tmp + val
            return self.running_sum / self.size
