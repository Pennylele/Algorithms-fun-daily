# create a dictionary out of the special 2D list
# while
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def find_lowest_price(needs):
            # memorization
            if tuple(needs) in self.memo:
                return self.memo[tuple(needs)]
            
            # For each dfs round, we should calculate the total cost without offers
            cost = 0
            for i, need in enumerate(needs):
                cost += price[i] * need
                
            # loop through offers that satisfy the needs
            for offer in special:
                for i in range(len(needs)):
                    if needs[i] < offer[i]:
                        break
                else:
                    new_needs = [need - offer[i] for i, need in enumerate(needs)]
                    cost = min(cost, offer[-1] + find_lowest_price(new_needs))
            
            self.memo[tuple(needs)] = cost
            return cost
                        
        
        self.memo = {}
        return find_lowest_price(needs)