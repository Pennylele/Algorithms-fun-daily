# Input: ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output: [null,1,1,1,1,0]

# [1,3,6,8] => [1,4,10,18]
class Solution:
    def __init__(self, w):
        self.prefix_sum = []
        self.total = 0

        for weight in w:
            self.total += weight # Be aware of what the self.total should be
            self.prefix_sum.append(self.total)

    def pickIndex(self):
        r = self.total * random.random() # Pay attention to how we get the random number.
        idx = bisect.bisect_left(self.prefix_sum, r)
        return idx
