# import bisect
# https://docs.python.org/3/library/bisect.html
# bisect.insort() is the same as bisect.insort_right()
class MyCalendarThree:
    def __init__(self):
        self.times = []
    
    def book(self, start, end):
        bisect.insort(self.times, (start, 1))
        bisect.insort(self.times, (end, -1))

        ans, cur = 0, 0
        for k, v in self.times:
            cur += v
            ans = max(ans, cur)
        return ans
