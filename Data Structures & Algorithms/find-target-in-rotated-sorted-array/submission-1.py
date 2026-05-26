class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target: # Target value found
                return mid
            if nums[low] <= nums[mid]: # Left Subarray
                if nums[mid] < target or target < nums[low]:
                    low = mid + 1
                else:
                    high = mid - 1
            


            else: # Right Subarray
                if nums[mid] > target or target > nums[high]:
                    high = mid - 1
                else:
                    low = mid + 1

        return -1 


