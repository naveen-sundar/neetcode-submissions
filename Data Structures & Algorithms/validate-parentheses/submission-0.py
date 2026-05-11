class Solution:
    def isValid(self, s: str) -> bool:
        closetoopen = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        if len(s) % 2 != 0: # If odd  length, return False since there needs to be a pair of parentheses
            return False
        stack = []
        for i in s:
            if i in closetoopen: # If stack is empty and closed parenthesis, no way of completion so False is returned
                if stack and (stack[-1] == closetoopen[i]): # If there is a open bracket for the following closed bracket encountered, we can pop the open bracket counterpart
                    stack.pop()
                else:
                    return False
            else: # Open parenthesis are appended to the stack
                stack.append(i)
        if stack == []:
            return True
        else:
            return False
        # O(n) Time and Space complexity
                    

