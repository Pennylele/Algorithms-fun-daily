# can use bisect, but probably not a good idea..
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        l = len(nums1) + len(nums2)
        if l % 2 != 0:
            return self.findMedian(nums1, nums2, l // 2)
        else:
            return (self.findMedian(nums1, nums2, l // 2 - 1) + self.findMedian(nums1, nums2, l // 2)) / 2
    
    def findMedian(self, A, B, k):
        if len(A) > len(B):
            A, B = B, A
        if not A:
            return B[k]
        if k == len(A) + len(B) - 1:
            return max(A[-1], B[-1])
        
        i = len(A) // 2 # since A's length is smaller than B, k - i would always be positive
        j = k - i

        if A[i] > B[j]:
            return self.findMedian(A[:i], B[j:], k - j) # we removed j elements, because i + j = k
        else:
            return self.findMedian(A[i:], B[:j], k - i) # we removed i elements
        

