# addRange(10, 20): null
# removeRange(14, 16): null
# queryRange(10, 14): true (Every number in [10, 14) is being tracked)
# queryRange(13, 15): false (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
# queryRange(16, 17): true (The number 16 in [16, 17) is still being tracked, despite the remove operation)
import bisect

class RangeModule:
    def __init__(self):
        self.container = []

    def addRange(self, left, right):
        #[10, 20, 30, 40] addRange(15, 35)
        l = bisect.bisect_left(self.container, left)
        r = bisect.bisect_right(self.container, right)

        tmp = []
        if l % 2 == 0:
            tmp.append(left)
        if r % 2 == 0:
            tmp.append(right)
        self.container[l:r] = tmp
            
    
    def removeRange(self, left, right):
        #[10, 20, 30, 40] removeRange(15, 35)
        l = bisect.bisect_left(self.container, left) # 1
        r = bisect.bisect_right(self.container, right) # 3

        tmp = []
        if l % 2 != 0:
            tmp.append(left)
        if r % 2 != 0:
            tmp.append(right)
        self.container[l:r] = tmp

    def queryRange(self, left, right):
        #[10, 20, 30, 40] removeRange(10, 20)
        l = bisect.bisect_right(self.container, left)
        r = bisect.bisect_left(self.container, right)

        if l == r and l % 2 != 0:
            return True
        else:
            return False


