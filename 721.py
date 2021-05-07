# Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Explanation:
# The first and third John's are the same person as they have the common email "johnsmith@mail.com".
# The second John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

# we need an email map as well as a user map.
# Time complexity - O(nlogn) where n is the # of strings in accounts

import collections

class Solution:
    def accountsMerge(self, accounts):
        emailMap = collections.defaultdict(set)
        userMap = {}
        
        # build the map
        for acc in accounts:
            for email in acc[1:]:
                emailMap[acc[1]].add(email)
                emailMap[email].add(acc[1])
                userMap[email] = acc[0]

        # dfs method
        def dfs(email, path):       
            for nei in emailMap[email]:
                if nei not in self.visited: 
                    self.visited.add(nei) # Please pay attention that we add the email to the self.visited inside the if statement, so that the email itself can be added to the path.
                    path.append(nei)
                    dfs(nei, path)
            return path
        
        # start dfs and build the ans
        self.visited = set()
        ans = []
        for email in emailMap:
            if email not in self.visited:
                tmp = dfs(email, [])
                ans.append([userMap[email]] + sorted(tmp))
        return ans

obj = Solution()
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
print(obj.accountsMerge(accounts))



