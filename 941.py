# I think the answer from the Solution is easier than mine.
class Solution:
    def validMountainArray(self, arr):
        N = len(arr)
        i = 0
        
        # ascending
        while i < N-1 and arr[i] < arr[i+1]:
            i += 1
        
        if i == 0 or i == N-1:
            return False
        
        # descending
        while i < N-1 and arr[i] > arr[i+1]:
            i += 1
        
        return i == N-1
        
# My method
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        A = len(arr)
        
        ascending_mountain = False
        descending_mountain = False
        # ascending array
        while i < A-1:
            if arr[i] < arr[i+1]:
                ascending_mountain = True
            elif arr[i] > arr[i+1]:
                descending_mountain = True
                break
            else: # arr[i] == arr[i+1]
                return False
            i += 1
        
        # descending array
        while i < A-1:
            if arr[i] < arr[i+1] or arr[i] == arr[i+1]:
                return False
            else:
                i += 1
        
        return ascending_mountain and descending_mountain