class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(mid):
            curSum = 0
            subarray = 0
            for elem in nums:
                curSum += elem
                if curSum > mid:
                    curSum = elem
                    subarray += 1



            return subarray + 1 <= k

        l, r = max(nums), sum(nums)
        res = r
        while l<=r:
            mid = (l + r) // 2

            if canSplit(mid):
                res = mid 
                r = mid - 1
            else:l = mid + 1

        return res
