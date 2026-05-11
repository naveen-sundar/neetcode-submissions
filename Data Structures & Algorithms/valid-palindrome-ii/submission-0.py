class Solution:
        def validPalindrome(self, s: str) -> bool:
            # Lowercase English letters
            if self.palindrome(s):
                return True
            for i in range(len(s)):
                new_string = s[:i]+s[i+1:]
                if self.palindrome(new_string):
                    return True
            return False

        def palindrome(self, string: str) -> bool:
            l = 0
            r = len(string)-1
            while l<r:
                if string[l] != string[r]:
                    return False

                l +=1
                r -=1
            return True
    
