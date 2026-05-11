class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs: # If empty list entered
            return ""
        
        comparison_string = strs[0] # Comparision string as the first
        for string in strs[1:]: # Traversing from second string to the end
            while comparison_string != string[:len(comparison_string)]: # If the second is not equal to the first one from the first to the last character
    
                comparison_string = comparison_string[:-1] # Reduce the length of the comparison string by one to see if there is any common prefix assuming first that the string itself is the common prefix (longest possible case)
        if comparison_string == "":
            return ""
        else:
            return comparison_string
            
            
              
