# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Time and space complexity: O(N*M^2), N is the length of wordList, M is the length of each word
# I'm thinking if we need to print the path: maybe we can store info in a dictionary - key as the parent word and the value is a list of next potential words. Then we do a DFS to get the path...
import collections, string
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if beginWord == endWord: return 0
        wordList = set(wordList)        
        if endWord not in wordList: return 0

        seen = set()
        q = collections.deque([(beginWord, 1)])
        all_alph = string.ascii_lowercase

        all_matches = []
        while q:
            word, step = q.popleft()
            if word == endWord:
                return step
            for i in range(len(word)):
                for j in all_alph:
                    new_word = word[:i] + j + word[i+1:]
                    if new_word not in seen and new_word in wordList:
                        seen.add(new_word)
                        q.append((new_word, step+1))
                        all_matches.append(new_word)
                print(all_matches)
        return 0

obj = Solution()
beginWord = "hit" 
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(obj.ladderLength(beginWord, endWord, wordList))



