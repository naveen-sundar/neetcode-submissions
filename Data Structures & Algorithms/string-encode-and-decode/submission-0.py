class Solution:

    def encode(self, strs: List[str]) -> str:
        return_string = ""
        for string in strs:
            return_string += str(len(string)) + "$" + string
        return return_string

    def decode(self, s: str) -> List[str]:
        res_array = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "$":
                j +=1 
            length_string = int(s[i:j])

            res_array.append(s[j+1 : j+1+length_string])
            i = j + 1 + length_string
        return res_array
