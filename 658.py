# Using binary search - searching for the leftmost element
# or those who are finding it hard to understand x - A[mid] > A[mid + k] - x think in terms of midpoint of the two values x > (A[mid + k] + A[mid])/2.
class Solution:
    def findClosestElements(self, arr, k, x):
        l, r = 0, len(arr)-k
        while l < r:
            mid = l + (r - l)//2
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid
        return arr[l: l + k]