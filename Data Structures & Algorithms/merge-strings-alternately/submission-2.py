class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        result= ""
        for i in range(len(word1)):
            result += word1[i]
            
            if len(word2) > i:
                result += word2[i]
            
        if len(word2) > len(word1):
            result = result + word2[i+1:]
        return result