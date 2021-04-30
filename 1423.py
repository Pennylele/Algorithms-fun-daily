class Solution:
    def maxScore(self, cardPoints, k):
        # sliding wnidow of k from cardPoints[:k] to cardPoints[-k:]
        curr = MAX = sum(cardPoints[:k]) # 6

        j = len(cardPoints)-1
        for i in range(k-1, -1, -1):
            curr = curr - cardPoints[i] + cardPoints[j]
            MAX = max(MAX, curr)
            j -= 1
        return MAX

s = Solution()
# cardPoints, k = [1,2,3,4,5,6,1], 3
cardPoints, k = [9,7,7,9,7,7,9], 7
print(s.maxScore(cardPoints, k))