class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_set = set(nums)
        maximum = 0
        
        for i in nums:
            s = 0
            if (i-1) not in new_set:
                while (s+i) in new_set:
                    s += 1
                if s > maximum:
                    maximum = s
        return maximum
                
