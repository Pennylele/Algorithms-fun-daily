# I think follow-up should be the below code with Counter and hashmap, not the sort method.
class Solution:
    def isAnagram(self, s, t):
        if collections.Counter(s) == collections.Counter(t):
            return True
        return False