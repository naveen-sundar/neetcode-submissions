class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Window length is one greater than k (see first test case)
        window = set()
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False
