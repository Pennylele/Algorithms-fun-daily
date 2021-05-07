class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        dp = {-1: 0}
        arr2.sort()
        
        for num in arr1:
            tmp = collections.defaultdict(lambda: float('inf')) # recording each state
            for key in dp: # result from the previous state
                if num > key: # potential next state
                    tmp[num] = min(tmp[num], dp[key]) # The value records the min changes to get a ascending list so far - finding the minimum dp[key] to be assigned to.
                loc = bisect.bisect_right(arr2, key) # for each key, we find a possible follower in arr2; and then write it into the tmp current state.
                if loc < len(arr2):
                    tmp[arr2[loc]] = min(tmp[arr2[loc]], dp[key] + 1) # This key in tmp should have a value that's a minimum dp[key] + 1, cause it's one more change.
            dp = tmp
        if dp:
            return min(dp.values())
        else:
            return -1
        
# 1 -1 {-1: 0}
# 5 1 defaultdict(<function Solution.makeArrayIncreasing.<locals>.<lambda> at 0x7f9ec030da60>, {1: 0})
# 3 5 defaultdict(<function Solution.makeArrayIncreasing.<locals>.<lambda> at 0x7f9ebfc28f70>, {5: 0, 2: 1})
# 3 2 defaultdict(<function Solution.makeArrayIncreasing.<locals>.<lambda> at 0x7f9ebfc28f70>, {5: 0, 2: 1})
# 6 3 defaultdict(<function Solution.makeArrayIncreasing.<locals>.<lambda> at 0x7f9ec030da60>, {3: 1})
# 7 6 defaultdict(<function Solution.makeArrayIncreasing.<locals>.<lambda> at 0x7f9ebfc28f70>, {6: 1, 4: 2})
# 7 4 defaultdict(<function Solution.makeArrayIncreasing.<locals>.<lambda> at 0x7f9ebfc28f70>, {6: 1, 4: 2})