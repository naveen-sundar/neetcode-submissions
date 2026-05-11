class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm ={} # Hashmap to store frequencies of characters
        arr = [[] for i in range(len(nums)+1)]
        output = []
        for i in nums:
            if i in hm:
                hm[i] += 1
            else:
                hm[i] = 1

        for key, value in hm.items():
            arr[value].append(key)

        for i in range(len(arr)-1, 0 ,-1):
            for n in arr[i]:
                output.append(n)
                if k == len(output):
                    return output


