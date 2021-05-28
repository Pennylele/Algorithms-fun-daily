# Two Pointer
class Solution:
    def isSubsequence(self, s, t):
        left_bound, right_bound = len(s), len(t)

        left, right = 0, 0
        while left < left_bound and right < right_bound:
            if s[left] == t[right]:
                left += 1
            right += 1
        return left == left_bound
# Follow-up
class Solution:
    def isSubsequence(self, s, t):
        t_map = collections.defaultdict(list)
        for i, ch in enumerate(t):
            t_map[ch].append(i)
        
        prev = -1 
        for ch in s:
            if ch not in t_map:
                return False
            indices_list = t_map[ch] # {a:[0], c:[5], b:[2]}
            idx = bisect.bisect_right(indices_list, prev) # 0
            if idx > len(indices_list) - 1:
                return False
            prev = indices_list[idx] # don't forget this should be the current ch's idx
        return True