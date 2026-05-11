class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(int) # Linear time and constant space

        for i in nums:
            
            hashmap[i] += 1
            if len(hashmap) <=2:
                continue
            new_hashmap = defaultdict(int)
            for i in hashmap:
                if hashmap[i] > 1:
                    new_hashmap[i] = hashmap[i] - 1 # 1's implicitly decremented
            
            hashmap = new_hashmap
        res = []
        for i in hashmap:
            if nums.count(i) > len(nums) // 3: # Use the original array to check
                res.append(i)
        return res
                