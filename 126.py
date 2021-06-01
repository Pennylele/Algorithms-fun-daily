# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
# Explanation: There are 2 shortest transformation sequences:
# "hit" -> "hot" -> "dot" -> "dog" -> "cog"
# "hit" -> "hot" -> "lot" -> "log" -> "cog"
# I think the time complexity should be O(M^2 * N) as well where M is the length of each word and N is the length fo the wordList
import collections
class Solution:
    def findLadder(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        layer = {}
        if endWord not in wordList: return []
        layer[beginWord] = [[beginWord]] # {"hit": [["hit"]]} one word may have several lists -recording the path so far}
        res = []

        while layer:
            new_layer = collections.defaultdict(list) # new_layer is updated every round. a word chain that cannot grow any longer would be gone
            for word in layer: # each word in layer is the last word in the word chain so far
                if word == endWord:
                    res.extend(k for k in layer[word]) # loop used since some word has several paths
                for i in range(len(word)):
                    for j in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + j + word[i+1:]
                        if new_word in wordList:
                            new_layer[new_word] += [w + [new_word] for w in layer[word]] # w is a list - adding the new_word to each of the lists from new_layer[new_word]
            wordList -= set(new_layer.keys()) # learned something new - can remove the used keys here.
            layer = new_layer
        return res

obj = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(obj.findLadder(beginWord, endWord, wordList))

