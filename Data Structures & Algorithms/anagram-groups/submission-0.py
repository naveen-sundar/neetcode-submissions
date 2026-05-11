from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in strs:
            characters = [0] * 26
            for character in i:
                count = ord(character) - ord("a")
                characters[count] += 1
            hashmap[tuple(characters)].append(i)
        
        return list(hashmap.values())


