class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(int)
        result = []
        for i in nums:
            
            hashmap[i] += 1

            
            if len(hashmap) <=2:
                continue
            new_hashmap = defaultdict(int)
            for i in hashmap:
                if hashmap[i] > 1:
                    new_hashmap[i] = hashmap[i]-1
            hashmap = new_hashmap
        for i in hashmap:
            if nums.count(i) > len(nums) // 3:
                result.append(i)
        return result


