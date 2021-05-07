class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        def distance(p1, p2):
            return (p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2
        
        candidates = [p1, p2, p3, p4]
        candidates.sort() # In this way, we can sort the points based on x, then p1 and p4 would be on the diagonal.
        diagonal_1 = distance(candidates[0], candidates[3])
        diagonal_2 = distance(candidates[1], candidates[2])
        edge_1 = distance(candidates[0], candidates[1])
        edge_2 = distance(candidates[0], candidates[2])
        
        return diagonal_1 == diagonal_2 and edge_1 == edge_2 and diagonal_1