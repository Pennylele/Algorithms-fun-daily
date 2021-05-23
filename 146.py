# Capacity is the limit
# LRU rule: everytime we operate on a key-value pair, we update its position (end of the chain)
# def put() => adding the new element into the end of the chain
# If the capacity is violated, we pop out the first element in the chain
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.orderedDict = collections.OrderedDict()

    def get(self, key):
        if key not in self.orderedDict:
            return -1
        else:
            self.orderedDict.move_to_end(key)
            return self.orderedDict[key]
    
    def put(self, key, value):
        if key not in self.orderedDict and len(self.orderedDict) >= self.capacity:
            self.orderedDict.popitem(False)
            self.orderedDict[key] = value
        else:
            self.orderedDict[key] = value
            self.orderedDict.move_to_end(key)
        