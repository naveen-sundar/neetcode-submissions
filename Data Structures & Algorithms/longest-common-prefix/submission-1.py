class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        for i in strs[1:]:
            while first != i[:len(first)]:
                first = first[:-1]
        return first
                