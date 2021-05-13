class Solution:
    def characterReplacement(self, s, k):
        counter = collections.Counter()
        left = 0
        cur_most_freq = 0

        for right in range(len(s)):
            counter[s[right]] += 1
            if counter[s[right]] > cur_most_freq: # Using a variable to track the most common char is must faster than the most_common() method
                cur_most_freq = counter[s[right]]
            if right - left + 1 - cur_most_freq > k: # The window only expands never shrinks. So that's why we can just return right - left + 1 in the end. And we also just loop through the array one element at a time
                counter[s[left]] -= 1
                left += 1
        return right - left + 1
#///////////////////////////////////////////////////////////////////
# class Solution:
#     def characterReplacement(self, s, k):
#         counter = collections.Counter()
#         left = 0
#         MAX = 0

#         for right in range(len(s)):
#             counter[s[right]] += 1
#             max_char_n = counter.most_common(1)[0][1]
#             if right - left + 1 - max_char_n > k:
#                 cur_max = right - left
#                 MAX = max(MAX, cur_max)
#                 counter[s[left]] -= 1
#                 left += 1
#         return MAX
        