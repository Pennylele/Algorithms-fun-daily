# The brute force would be O(n^2)
# We can use the fenwick tree method to make it O(nlogn)
# if we rank the numbers based on their numerical value, and then fill out the fenwick tree with how many of them are ahead of the current number with nlogn time
class Solution:
    def countSmaller(self, nums): # example: [5,2,6,1]
        rank = {value: i+1 for i, value in enumerate(sorted(nums))} # {1: 1, 2: 2, 5: 3, 6: 4}
        N = len(nums)
        BITTree = [0] * (N+1)

        def getSum(idx):
            ans = 0
            while idx > 0:
                ans += BITTree[idx]
                idx -= (idx & -idx)
            return ans

        def update(idx):
            while idx < (N+1):
                BITTree[idx] += 1
                idx += (idx & -idx)

        res = []
        for x in reversed(nums): # [1,6,2,5]
            res.append(getSum(rank[x]-1))
            update(rank[x])
        return res[::-1] # don't forget to reverse it