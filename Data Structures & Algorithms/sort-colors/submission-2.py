class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Two pass, O(n), O(1) Time and space solution
        freq = [0, 0, 0]
        for i in nums: # O(n) time complexity
            freq[i] += 1 # freq array contains the frequencies of three elements
        
        i = 0
        for n in (0, 1, 2):
            for j in range(freq[n]):
                nums[i] = n
                i += 1
            
