# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
#//////////////////////////vanilla backtracking/////////////////////////////////
class Solution:
    def combinationSum(self, candidates, target):
        def backtrack(candidates, start, path, target):
            if target == 0:
                res.append(path[:])
                return
            if target < 0:
                return 
            for i in range(start, C):
                target -= candidates[i]
                path += [candidates[i]]
                backtrack(candidates, i, path, target)
                target += candidates[i]
                path.pop()

        res = []
        C = len(candidates)
        backtrack(candidates, 0, [], target)
        return res
#//////////////////////////backtracking + pruning/////////////////////////////////
class Solution:
    def combinationSum(self, candidates, target):
        def backtrack(candidates, start, path, target):
            if target == 0:
                res.append(path)
                return False
            if target < 0:
                return True
            for i in range(start, C):
                if backtrack(candidates, i, path + [candidates[i]], target - candidates[i]):
                    break

        res = []
        C = len(candidates)
        candidates.sort()
        backtrack(candidates, 0, [], target)
        return res

obj = Solution()
print(obj.combinationSum([2,3,6,7], 7))