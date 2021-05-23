class Leaderboard:

    def __init__(self):
        self.scoreboard = collections.Counter()
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.scoreboard:
            self.scoreboard[playerId] += score
        else:
            self.scoreboard[playerId] = score
        

    def top(self, K: int) -> int:
        most_common_k = self.scoreboard.most_common(K) # most_common() is a O(nlogn) algorithm - probably the same as using heap
        return sum([i[1] for i in most_common_k])
        

    def reset(self, playerId: int) -> None:
        del self.scoreboard[playerId]