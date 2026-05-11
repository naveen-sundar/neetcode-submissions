class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): # Edge case
            return False

        def characters(string):
            arr = [0]*26
            for i in string:
                
                arr[ord(i) - ord('a')] += 1
            
            return arr
        
        ref = characters(s1)
        window = characters(s2[:len(s1)])
        
        if ref == window:
            return True
        
        for i in range(len(s1), len(s2)):
            start_index = i - len(s1)
            end_index = i
            window[ord(s2[start_index]) - ord('a')] -= 1
            window[ord(s2[end_index]) - ord('a')] += 1



            if ref == window:
                return True
        return False
            
        
