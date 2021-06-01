# Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
#graph = {"JFK":["SFO", "ATL"], "SFO": ["ATL"], "ATL": ["JFK", "SFO"]}
# This is the situation when we are sure there's an anwer - Euler Tour.
# Otherwise we may need to validate it's a valid Euler Tour first.
class Solution:
    def findItinerary(self, tickets):
        graph = collections.defaultdict(list)
        tickets = sorted(tickets, key=lambda x: x[1], reverse=True)

        for FROM, TO in tickets:
            graph[FROM].append(TO)
        
        def dfs(stop):
            des_list = graph[stop]
            while des_list:
                nxt = des_list.pop()
                dfs(nxt)
            itinerary.append(stop)

        itinerary = []
        start = "JFK"
        dfs(start)
        return itinerary[::-1]

    