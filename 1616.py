class Solution:
    def checkPalindromeFormation(self, a, b):
        l, r = 0, len(a)-1
        while l < r and a[l] == b[r]:
            l += 1
            r -= 1
        s1, s2 = a[l:r+1], b[l:r+1]
        
        l, r = 0, len(a)-1
        while l < r and b[l] == a[r]:
            l += 1
            r -= 1
        s3, s4 = a[l:r+1], b[l:r+1]
        
        for s in (s1, s2, s3, s4):
            if s == s[::-1]:
                return True
        return False