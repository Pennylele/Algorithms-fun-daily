# people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
# I think there are multiple O(n^2) solutions, O(nlogn) is more difficult to think of. I haven't delved deeper into a potential fenwick tree solution.
class Solution(object):
    def reconstructQueue(self, people):
        people.sort(key=lambda x: (-x[0], x[1]))

        ans = []
        for i in range(len(people)):
            loc = people[i][1]
            ans.insert(loc, people[i])
        return ans

obj = Solution()
print(obj.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))