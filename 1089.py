class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = arr.count(0)
        n = len(arr)
        
        for i in range(n-1, -1, -1):
            if i + zeros < n:
                arr[i + zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = 0 # think of this example [1,0,2,0,3,0] => for the 2nd 0, after changing the last element to be 0, the previous element before the last element shoule be 0 too since we only changed the duplicated position.
        return arr