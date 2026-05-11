class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = {}
        hmap2 = {}
        if len(s) == len(t):
            for i in s:
                if i not in hmap:
                    hmap[i] = 1
                else:
                    hmap[i] += 1
            for i in t:
                if i not in hmap2:
                    hmap2[i] = 1
                else:
                    hmap2[i] += 1
            if hmap == hmap2:
                return True
            else:
                return False
        else:
            return False