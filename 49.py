# Time complexity: O(nk) where n is the number of strings and k is the average length of each string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for string in strs:
            counting = [0] * 26
            for ch in string:
                key = ord(ch) - ord('a')
                counting[key] += 1
            d[tuple(counting)].append(string) # need to make sure the key is a tuple
        return d.values()