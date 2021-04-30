# (10, 20), ()
import bisect

class MyCalendar:
    def __init__(self):
        self.start = []
        self.end = []
           
    def book(self, start, end):
        idx = bisect.bisect_left(self.start, start)
        if idx >= 1:
            if start < self.end[idx - 1]:
                return False
        if idx < len(self.end):
            if end > self.start[idx]:
                return False
        self.start.insert(idx, start)
        self.end.insert(idx, end)
        return True
        

