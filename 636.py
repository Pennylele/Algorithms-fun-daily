# We can use a stack to track the last excuted ID
# when we see start - the prev execution is done; we also append the new/latest ID to the stack (it can be the same as the prev ID or not)
# When we see end - we get the current ID by popping it out from the stack and write it to the final answer based on the idx/ID. update the prev_time as well for future calculations.
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        ans = [0] * n
        prev_time = 0
        
        for log in logs:
            ID, typ, time =  log.split(':')
            ID, time = int(ID), int(time)
            
            if typ == "start":
                if stack:
                    ans[stack[-1]] += time - prev_time
                stack.append(ID)
                prev_time = time
            else:
                ans[stack.pop()] += time - prev_time + 1 # this line works because there's a garantee that the ID popped matches the current ID
                prev_time = time + 1
        return ans