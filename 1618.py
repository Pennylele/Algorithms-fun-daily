class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo : 'FontInfo') -> int:
        def check(fs):
            if fontInfo.getHeight(fs) > h:
                return False
            if sum(fontInfo.getWidth(fs, i) for i in text) > w:
                return False
            return True            
        
        F = len(fonts)
        l, r = -1, F-1
        while l < r:
            mid = r - (r - l) // 2 # This should be similar to bisect_right
            #print(mid)
            fontsize = fonts[mid]
            if check(fontsize):
                l = mid
            else:
                r = mid-1
        return -1 if l == -1 else fonts[l]
        