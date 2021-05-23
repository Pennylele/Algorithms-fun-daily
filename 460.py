# Use a dictionary to store the key value pairs. key is the key, value is the Node (which has key, value, and count) - for O(1) get
# self.countFreq is a defaultdict(OrderedDict) where the key is the freq count, and value is the OrderedDict who has the key-value pairs. - for updating and keeping track of the counter/freq count
# Each key value element is a Node who has a key attribute, a value attribute, and a count attribute (yes keeping its own count, so that we can locate it in the self.countFreq)
# also a minFreq - this is to make sure that remove the LFU in O(1)
class Node:
    def __init__(self, key, val, count):
        self.key = key
        self.val = val
        self.count = count

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.d = {}
        self.countFreq = collections.defaultdict(OrderedDict)
        self.minFreq = 0

    
    def get(self, key):
        if key not in self.d:
            return -1
        node = self.d[key]
        count = node.count
        

        # update the node freq
        del self.countFreq[count][key]
        
        # remove the node.count key value pair if node.count key's value is 0
        if not self.countFreq[count]:
            del self.countFreq[count]
            
        node.count += 1
        self.countFreq[node.count][key] = node


        # update the minFreq if necessary
        if not self.countFreq[self.minFreq]:
            self.minFreq += 1

        return node.val
        
        
    def put(self, key, value):
        if key in self.d:
            self.d[key].val = value
            self.get(key)
            return
        
        if not self.capacity: return 0
        
        if self.capacity == len(self.d):
            k, v = self.countFreq[self.minFreq].popitem(last=False)
            del self.d[k]
        new_node = Node(key, value, 1)
        self.d[key] = new_node
        self.countFreq[1][key] = new_node
        self.minFreq = 1
        return