class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        leading_count = float('-inf')
        leader = None
        vote_count = collections.Counter()
        self.memo = []
        self.times = times
        
        for i in range(len(persons)):
            vote_count[persons[i]] += 1
            if vote_count[persons[i]] >= leading_count:
                leading_count = vote_count[persons[i]]
                leader = persons[i]                
            self.memo.append([times[i], leader])
        print(self.memo)
        
    def q(self, t: int) -> int:
        idx = bisect.bisect_right(self.times, t) - 1
        return self.memo[idx][1]

# From this problem, I learned that bisect behaves differently among searching for a 1D array and a 2D array:
>> lst = [0,5,10,15,20,25,30]
>> idx = bisect.bisect(lst, 25) # behaves the same as the bisect_right
>> idx
6
>> lst = [0,5,10,15,20,25,30]
>> idx = bisect.bisect_left(lst, 25) # behaves the same as the bisect_right
>> idx
5
>> lst = [[0, 0], [5, 1], [10, 1], [15, 0], [20, 0], [25, 1], [30, 0]]
>> idx = bisect.bisect(lst, [25])
>> idx
5
>> lst = [[0, 0], [5, 1], [10, 1], [15, 0], [20, 0], [25, 1], [30, 0]]
>> idx = bisect.bisect_left(lst, [25])
>> idx
5
>> lst = [[0, 0], [5, 1], [10, 1], [15, 0], [20, 0], [25, 1], [30, 0]]
>> idx = bisect.bisect_right(lst, [25])
>> idx
5