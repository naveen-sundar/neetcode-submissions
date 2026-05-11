class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxLength = 0
        hashset = set()
        while r < len(s):
            if s[r] not in hashset:
                hashset.add(s[r])
                
                if (r - l + 1) > maxLength:
                    maxLength = r - l + 1
                r += 1
            else:
                hashset.remove(s[l])
                l += 1
        return maxLength
            
