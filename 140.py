class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        def dfs(s):
            if s in memo:
                return memo[s]
            if not s:
                return [[]]
            
            cur_word_breaks = []
            
            for i in range(len(s)):
                new_word = s[:i+1]
                
                if s[:i+1] in wordSet:
                    new_word_breaks = dfs(s[i+1:])
                    for rest_words in new_word_breaks:
                        cur_word_breaks.append([new_word] + rest_words)
            
            memo[s] = cur_word_breaks 
            return cur_word_breaks
            
        wordSet = set(wordDict)
        memo = {}
        word_breaks = dfs(s)
        return [' '.join(words) for words in word_breaks]