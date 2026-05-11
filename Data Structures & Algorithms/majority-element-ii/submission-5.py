class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash_set = {}
        result = []
        required_freq = len(nums) // 3
        for i in nums:
            if i in hash_set:
                hash_set[i] +=1
            else:
                hash_set[i] = 1
        for i in hash_set:
            if hash_set[i] > required_freq:
                result.append(i)
        return result
                
