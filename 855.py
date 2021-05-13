class ExamRoom:

    def __init__(self, N):
        self.N, self.seats = N, []

    def seat(self):
        N, S = self.N, self.seats
        if not S: res = 0
        else:
            d, res = S[0], 0
            for a, b in zip(S, S[1:]):
                if (b - a) // 2 > d:
                    d, res = (b - a) // 2, (b + a) // 2
            if N - 1 - S[-1] > d: res = N - 1
        bisect.insort(S, res)
        return res

    def leave(self, p):
        self.seats.remove(p)
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)