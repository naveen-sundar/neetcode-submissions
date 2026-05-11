class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            dict =  {}
            dict2 = {}
            for i in s:
                if i in dict:
                    dict[i] +=1
                else:
                    dict[i] = 1
            for j in t:
                if j in dict2:
                    dict2[j] +=1
                else:
                    dict2[j] = 1
            if dict == dict2:
                return True
            else:
                return False                

        else:
            return False