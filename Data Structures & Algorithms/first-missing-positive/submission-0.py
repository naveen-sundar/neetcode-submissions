class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        maximum = 0
        hashmap = {}
        for i in nums:
            if i > 0:
                if i > maximum:
                    maximum = i
                hashmap[i] = hashmap.get(i, 0) + 1

        if maximum == 0:
            return 1
        # Maximum stores the positive maximum value
        for i in range(1, maximum): 
            if i not in hashmap:
                return i
        return maximum + 1
        
