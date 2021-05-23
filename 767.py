# can use heaps for this problem. We just need to see if we can assign every other elements differently.
# Example 1:
# Input: s = "aab"
# Output: "aba"
# Example 2:

# Input: s = "aaab"
# Output: ""
import collections, heapq
class Solution:
    def reorganizeString(self, S):
        d = collections.Counter(S)
        hq = [(-value, key) for key, value in d.items()]
        heapq.heapify(hq)

        p_v = 0
        ans = []
        while hq:
            v, k = heapq.heappop(hq)
            ans.append(k)
            if p_v < 0:
                heapq.heappush(hq, (p_v, p_k)) # if the p_v == 0, we won't push the previous key any longer
            v += 1
            p_v, p_k = v, k
        
        if len(ans) != len(S):
            return ''
        else:
            return ''.join(ans)

obj = Solution()
print(obj.reorganizeString('aaab'))
print(obj.reorganizeString('aab'))
