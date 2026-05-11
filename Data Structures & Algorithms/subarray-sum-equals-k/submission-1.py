class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        curSum = 0
        dictionary = {0:1}
        for i in nums:
            curSum += i
            if curSum-k in dictionary:
                result += dictionary[curSum - k]


            dictionary[curSum] = dictionary.get(curSum, 0) + 1
    
        return result