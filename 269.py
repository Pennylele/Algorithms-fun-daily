# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"
# t > f; w > e; r > t; e > r
# building a dictionary: {t:[f], w:[e], r:[t], e:[r]} 
# Good candidate for topological sort
class Solution:
    def alienOrder(self, words):
        # building indegrees and outdegrees
        outdegrees = collections.defaultdict(set)
        indegrees = {c: 0 for word in words for c in word} # wrote it wrong

        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in outdegrees[c1]:
                        outdegrees[c1].add(c2)
                        indegrees[c2] += 1
                    break
            else: # See how this else is used
                if len(w1) > len(w2): return '' # edge case

        # start peeling the onion
        ans = []
        queue = collections.deque([c for c in indegrees if indegrees[c] == 0]) # queue is needed in topological sort
        while queue:
            c = queue.popleft()
            ans.append(c)
            for nei in outdegrees[c]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)

        if len(ans) < len(indegrees):
            return ""
        else:
            return "".join(ans)


