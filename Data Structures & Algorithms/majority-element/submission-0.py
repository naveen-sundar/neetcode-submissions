class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority_frequency = n/2
        dict={}
        for index in range(n):
            if nums[index] not in dict:
                dict[nums[index]] = 1
            else:
                dict[nums[index]] +=1
        for key, value in dict.items():
            if value > majority_frequency:
                return key
        return "DummyValue"

            
            
