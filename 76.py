class Solution:
    def minWindow(self, s, t):
        # edge case
        if not s or not t: return ""

        # set up variables for t
        dict_t = collections.Counter(t) # count occurances of each char
        required = len(dict_t) # how many unique chars are there

        filtered_s = []
        for i, char in enumerate(s):
            if char in dict_t:
                filtered_s.append((i, char))
        
        l, r = 0, 0
        formed = 0 # counting towards the required
        window_counts = {}# track the occurances of each char and compare with dict_t

        ans = [float('inf'), None, None] # max_length, start, end
        while r < len(filtered_s):
            char = filtered_s[l][1]
            window_counts[char] = window_counts.get(char, 0) + 1
            if window_counts[char] == dict_t[char]:
                formed += 1
            
            # if the current window has all the required chars, we calculate the length now
            if l <= r and formed == required:
                char = filtered_s[l][1]

                end = filtered_s[r][0]
                start = filtered_s[l][0]
                if end - start + 1 > ans[0]:
                    ans[0], ans[1], ans[2] = end - start + 1, start, end

                window_counts[char] -= 1
                if window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]