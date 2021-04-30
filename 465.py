class Solution:
    def minTransfers(self, transactions):
        graph = collections.defaultdict(int)
        for p1, p2, amount in transactions:
            graph[p1] += amount
            graph[p2] -= amount
        
        balance_sheet = [v for k, v in graph.items() if v != 0]

        # backtrack function to find the minimum transactions
        def backtrack(start, sheet): # [-5, 10, -5]
            if start == len(sheet): return 0
            if sheet[start] == 0:
                return backtrack(start+1, sheet)
            MIN = float('inf')
            for i in range(start+1, len(sheet)):
                if sheet[start] * sheet[i] < 0:
                    sheet[i] += sheet[start]
                    MIN = min(MIN, backtrack(start+1, sheet) + 1)
                    sheet[i] -= sheet[start]

                    if sheet[i] + sheet[start] == 0: break
            return MIN
        

        return backtrack(0, balance_sheet)
