class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # General solution for K Sum
        nums.sort()
        res, quad = [], []
        

        def KSum(k,start, target):
            if k != 2: # Recursive Case
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i-1] == nums[i]:
                        continue
                    quad.append(nums[i])
                    KSum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return 
            l, r = start, len(nums) - 1
                    
            while l < r:
                s = nums[l] + nums[r]
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    res.append(quad + [nums[l] , nums[r]])
                    l += 1
                    while nums[l-1] == nums[l] and l < r:
                        l += 1
        KSum(4, 0, target)
        return res

