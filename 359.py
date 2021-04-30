class Logger:
    def __init__(self):
        self.messageQueue = {}
    
    def shouldPrintMessage(self, timestamp, message):
        if message not in self.messageQueue:
            self.messageQueue[message] = timestamp
            return True
        else:
            if timestamp - self.messageQueue[message] > 10:
                return True
            else:
                return False

# I think there's a followup questions for this problem. My guess is that they ask to clean up the messageQueue, in case there are many old outdated clutters. So below is one possible solution.
import collections.orderedDict()
class Logger:
    def __init__(self):
        self.messageQueue = collections.orderedDict()
    
    def shouldPrintMessage(self, timestamp, message):
        for mes, ts in self.messageQueue.items():
            if ts + 10 <= timestamp:
                self.messageQueue.pop(mes)
            if message in self.messageQueue:
                return False
            else:
                self.messageQueue[message] = timestamp
                return True
