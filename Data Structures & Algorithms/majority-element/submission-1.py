class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
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
        '''
        # Bayer Moore Majority Vote Algorithm

        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            if res == n:
                count +=1
            else:
                count -=1
        return res
            
            
