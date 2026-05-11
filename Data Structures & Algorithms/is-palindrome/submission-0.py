class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstring = ""
        for i in s:
            if i.isalnum():
                newstring += i.lower()
        
        return newstring == newstring[::-1]
    

        

