class Solution:
    def getCollisionTime(self, cars):
        C = len(cars)
        ans = [-1] * C
        stack = [(float('inf'), cars[-1][0], cars[-1][1])]

        for i in range(C-2, -1, -1):
            cur_p = cars[i][0]
            cur_s = cars[i][1]

            while stack and (cur_s <= stack[-1][2] or (stack[-1][1] - cur_p) / (cur_s - stack[-1][2]) > stack[-1][0]): # This is the condition when the current car wouldn't have collision with the next.
                stack.pop()
            
            if not stack:
                stack.append((float('inf'), cur_p, cur_s))
            else:
                curCollideTime = (stack[-1][1] - cur_p) / (cur_s - stack[-1][2])
                stack.append((curCollideTime, cur_p, cur_s))
                ans[i] = curCollideTime
        return ans
