class RLEIterator:

    def __init__(self, A: List[int]):
        self.A = A
        self.index = 0 # pointing to the current index in A
                
    def next(self, n: int) -> int:
        while self.index < len(self.A):
            if self.A[self.index] >= n:
                self.A[self.index] -= n
                return self.A[self.index + 1]
            else:
                n -= self.A[self.index]
                self.index += 2
        return -1
            