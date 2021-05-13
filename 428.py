#      1
#    / | \
#   3  2  4
#  / \
# 5   6
class WrappableInt: # This class is implemented bc the prob asks us to avoid using global/stateless variables.
    def __init__(self, x):
        self.value = x
    def getValue(self):
        return self.value
    def increment(self):
        self.value += 1

class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Codec:
    def serialize(self, root): # ['1', '3', '5', '#', '6', '#', '#', '2', '#', '4', '#', '#']
        data = [] # We didn't use self.data, because the prob asks us to avoid using global/stateless variables.
        self.__serializeHelper(root, data)
        return "".join(data)
    
    def __serializeHelper(self, node, data):
        if not node: return # missed writing this correctly
        data.append(chr(node.val + 48))
        for child in node.children:
            __serializeHelper(child, data)
        data.append("#")
        
    def deserialize(self, data):
        if not data: return None
        return self.__deserializeHelper(data, WrappableInt(0))
    
    def __deserializeHelper(self, data, idx):
        if idx.getValue() == len(data): return None # See how we interact with the WrappableInt

        node = Node(ord(data[idx.getValue()]) - 48, []) # have to initiate the empty list, otherwise we'd get the "can't append to None type error"
        idx.increment()
        while data[idx.getValue()] != "#":
            node.children.append(self.__deserializeHelper(data, idx))
        
        idx.increment()
        return node

#/////////////////////////////////////////////////////////////////////
# Thinking process for the chr() funciton
# This is a trick I learned in one of the fastest of Java solutions. Unfortunately, I don't have a profile to tag it with for credit here. The data provided to us in the nodes of the tree are integers. Sure, we can represent each integer as a string of digits. However, if we do that, then we would need some sort of a delimiter to separate the numbers themselves. After all 1234 could be 12 and 34 or it could be 1 and 234. Without a delimiter to separate them, the deserializer won't know.

# If we do add a delimiter, it would add to the length of the overall string, which is fine. However, in the deserializer then, we would have to use the split operation and form a list of strings (more like a queue since that is how we will process them) and that is a relatively costly operation in terms of time and not to mention the extra space that the list would use.

# Of course there are limitations to this approach:

#     Won't work on negative numbers
#     Won't work if the numbers are > 65536

# So, it's not really something that we can rely on 100% for correctness. It just so happens that for the test cases in this problem, this trick works perfectly fine and it is something to remember for solving other programming problems as well.