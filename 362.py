class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = [[0, i+1] for i in range(300)]

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        # although we are re-using the 300 elements, the timestamp may change.
        idx = (timestamp - 1) % 300
        if self.queue[idx][1] == timestamp:
            self.queue[idx][0] += 1
        else:
            self.queue[idx][0] = 1
            self.queue[idx][1] = timestamp

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        count = 0
        for hits, ts in self.queue:
            if timestamp - ts < 300:
                count += hits
        return count