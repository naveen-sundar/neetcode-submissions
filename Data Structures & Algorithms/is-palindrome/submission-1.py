class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not self.is_alphanumeric(s[i]):
                i += 1
            while i < j and not self.is_alphanumeric(s[j]):
                j -= 1            
            
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1 # Don't forget to see the pointer direcetion
        return True





    def is_alphanumeric(self, char):
        if ((ord("a") <= ord(char) <= ord("z")) or (ord("0") <= ord(char) <= ord("9")) or
            (ord("A") <= ord(char) <= ord("Z"))): # Full bracket for multiple conditions
            
            return True
        return False
        