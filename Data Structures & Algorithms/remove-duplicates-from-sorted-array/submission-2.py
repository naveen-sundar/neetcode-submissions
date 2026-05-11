class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr1 = len(nums)-1
        if len(nums)==1:
            return 1
        while ptr1 >=0:
            if nums[ptr1] == nums[ptr1-1]:
                del nums[ptr1]
            ptr1 -= 1
        return len(nums)