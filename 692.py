# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.
import collections, heapq
# class Solution:
#     def topKFrequent(self, words, k):
#         wordMap = collections.Counter(words)
#         ordered_wordMap = sorted(wordMap.items(), key=lambda x: (-x[1], x[0]))
#         return [x[0] for x in ordered_wordMap]
class Solution:
    def topKFrequent(self, words, k):
        elements = collections.Counter(words)
        hq = []
        res = []

        for word, freq in elements.items():
            heapq.heappush(hq, (-freq, word))
            if len(hq) > len(elements) - k:
                res.append(heapq.heappop(hq))
        return [x[1] for x in sorted(res)]

obj = Solution()
# print(obj.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
print(obj.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 3))