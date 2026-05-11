class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for index, val in enumerate(nums):
            
            if val in hmap:
                if hmap[val] != index:
                    return [hmap[val], index]
            hmap[target - val] = index
