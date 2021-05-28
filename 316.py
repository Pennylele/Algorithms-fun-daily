# optimization 1: continue through the visited set
# optimization 2: a stack to add potential candidate - but pop out the last element once we see a smaller element, but at same time, the last char in stack is not the only one left for its own kind
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d = collections.defaultdict(int)
        for idx, char in enumerate(s):
            d[char] = idx
        stack = ['!']
        visited = set()
        
        for i, char in enumerate(s):
            if char in visited: continue
            while char < stack[-1] and d[stack[-1]] > i:
                visited.remove(stack.pop())
            stack.append(char)
            visited.add(char)
        return ''.join(stack[1:])