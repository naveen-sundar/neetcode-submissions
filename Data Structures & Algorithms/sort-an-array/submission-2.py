class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.MergeSort(nums)
        
    
    def MergeSort(self, arr):
        if len(arr)<=1:
            return arr
        mid = len(arr)//2
        left_part = self.MergeSort(arr[:mid])
        right_part = self.MergeSort(arr[mid:])
        return self.Merge(left_part, right_part)
    
    def Merge(self, arr1, arr2):
        result = []
        i = j = 0
        
        while i < len(arr1) and j < len(arr2):
            if arr1[i] > arr2[j]:
                result.append(arr2[j])
                j +=1
            else:
                result.append(arr1[i])
                i +=1
        result.extend(arr1[i:])
        result.extend(arr2[j:])
        return result





    
       