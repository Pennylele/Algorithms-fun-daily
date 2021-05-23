class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        R, C = len(maze), len(maze[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        stack = [(start[0], start[1])]
        seen = {(start[0], start[1])}
        
        while stack:
            r, c = stack.pop()
            
            for d in directions:
                cur_r, cur_c = r, c
                while 0 <= cur_r < R and 0 <= cur_c < C and maze[cur_r][cur_c] == 0:
                    cur_r, cur_c = cur_r + d[0], cur_c + d[1]
                
                cur_r, cur_c = cur_r - d[0], cur_c - d[1]
                
                    
                if cur_r == destination[0] and cur_c == destination[1]:
                    return True
            
                if (cur_r, cur_c) not in seen:
                    seen.add((cur_r, cur_c))
                    stack.append((cur_r, cur_c))
        return False