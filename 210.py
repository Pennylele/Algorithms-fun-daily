# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
class Solution:
    def findOrder(self, numCourses, prerequisites):
        # creating the graph
        indegrees = {c: 0 for c in range(len(numCourses))}
        outdegrees = collections.defaultdict(list)

        for c1, c2 in prerequisites:
            indegrees[c1] += 1
            outdegrees[c2].append(c1)
        
        # find all the nodes without indegrees
        no_pre = []
        for c in indegrees:
            if indegrees[c] == 0:
                no_pre.append(c)

        # peeling the onion
        ans = []
        while no_pre:
            course = no_pre.pop()
            ans.append(course)
            for nei in outdegrees[course]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    no_pre.append(nei)
        
        if len(ans) == len(indegrees):
            return ans
        else:
            return [0]
