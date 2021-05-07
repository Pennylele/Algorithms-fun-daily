class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        m = int(log2(n)) + 1
        self.dp = [[-1] * m for _ in range(n)]
        
        for i in range(n):
            self.dp[i][0] = parent[i]
            
        for i in range(n):
            for j in range(1, m):
                if self.dp[i][j-1] != -1:
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1] # This is to populate dp[i][j] based on the dp's previous calculation on dp[dp[i][j-1]][j-1]. For example, if we calculate i to 2 ^ 4, then it should be equal to dp[dp[i][2^3]][2^3]

        # [[-1, -1, -1], 
        #  [0, -1, -1], 
        #  [0, -1, -1], 
        #  [1, 0, -1],  # dp[3][1] = dp[dp[3][0]][0]
        #  [1, 0, -1], 
        #  [2, 0, -1], 
        #  [2, 0, -1]]

    def getKthAncestor(self, node: int, k: int) -> int:
        while k > 0 and node != -1:
            j = int(log2(k))
            node = self.dp[node][j]
            k -= (1 << j)
        
        return node
