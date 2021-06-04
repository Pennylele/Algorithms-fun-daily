# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
import collections
class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = collections.defaultdict(list)
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        
        #0: not visited; -1: visiting; 1: visited
        visited = [0] * numCourses
        def dfs(start):
            if visited[start] == -1:
                return False
            if visited[start] == 1:
                return True
            visited[start] = -1
            for pre in graph[start]: # one dfs round
                if not dfs(pre):
                    return False
            visited[start] = 1
            return True


        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

obj = Solution()
print(obj.canFinish(2, [[1,0],[0,1]]))