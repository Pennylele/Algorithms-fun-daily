class MedianFinder:
    def __init__(self):
        self.smallHalf = [] # maxHeap
        self.largeHalf = [] # minHeap
   
    def addNum(self, num):
        if len(self.smallHalf) == len(self.largeHalf):
            s = heapq.heappushpop(self.smallHalf, -num)
            heapq.heappush(self.largeHalf, -s)
        else:
            l = heapq.heappushpop(self.largeHalf, num)
            heapq.heappush(self.smallHalf, -l)

    def findMedian(self):
        if len(self.smallHalf) == len(self.largeHalf):
            return (-self.smallHalf[0] + self.largeHalf[0]) / 2
        else:
            return self.largeHalf[0]
