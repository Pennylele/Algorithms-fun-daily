# Input: secret = "1123", guess = "0111"
# Output: "1A1B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1123"        "1123"
#   |      or     |
# "0111"        "0111"
# Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
import collections
class Solution:
    def getHint(self, secret, guess):
        # a dictinoary to keep track of the digit in secret
        counter = collections.defaultdict(int)
        bulls = cows = 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                if counter[secret[i]] < 0:
                    cows += 1
                if counter[guess[i]] > 0:
                    cows += 1
                counter[secret[i]] += 1
                counter[guess[i]] -= 1
        return str(bulls) + "A" + str(cows) + "B"

obj = Solution()
print(obj.getHint("1123", "0111"))