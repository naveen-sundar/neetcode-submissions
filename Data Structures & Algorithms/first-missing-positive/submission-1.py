class Solution:
    def firstMissingPositive(self, arr: List[int]) -> int:
        for i in range(len(arr)): # Replacing all negative values with zero in-place
            if arr[i] < 0:
                arr[i] = 0
        for i in range(len(arr)):
            value = abs(arr[i])
            if 1 <= value <= len(arr): # If the element in the array falls in the solution set
                
                if arr[value-1] > 0:
                    arr[value-1] = arr[value-1] * -1
                elif arr[value-1] == 0:
                    arr[value-1] = (len(arr) + 1) * -1

        for i in range(1, len(arr)+1): # Loops till len(arr)
            if arr[i-1] >= 0: # Greater than or equal to
                return i
        return len(arr) + 1




                

        