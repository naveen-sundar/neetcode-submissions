class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Merge sort can be performed.

        
        def Merge(left, right): # Merging two sorted arrays
            i = 0
            j = 0
            result = []
            while i < len(left) and j < len(right):
                if left[i]> right[j]:
                    result.append(right[j])
                    j += 1
                else:
                    result.append(left[i])
                    i += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        def MergeSort(nums):
            if len(nums) <=1:
                return nums
            mid = len(nums) // 2
            left_array = MergeSort(nums[:mid])
            right_array = MergeSort(nums[mid:])
            return Merge(left_array, right_array)
        sorted_nums = MergeSort(nums)
        for i in range(len(nums)):
            nums[i] = sorted_nums[i]