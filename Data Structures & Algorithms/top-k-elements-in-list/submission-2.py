class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}

        # Count frequencies correctly
        for i in nums:
            if i not in hmap:
                hmap[i] = 1
            else:
                hmap[i] += 1

        # Bucket sort
        count = [[] for _ in range(len(nums) + 1)]

        for key, value in hmap.items():
            count[value].append(key)

        res = []

        # Traverse buckets from high freq to low
        for i in range(len(count) - 1, 0, -1):
            for n in count[i]:
                res.append(n)

                if len(res) == k:
                    return res