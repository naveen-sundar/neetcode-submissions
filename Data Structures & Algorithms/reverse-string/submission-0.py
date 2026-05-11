class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        front_pointer = 0
        back_pointer = len(s)-1
        while front_pointer < back_pointer:
            s[front_pointer], s[back_pointer] = s[back_pointer], s[front_pointer]
            front_pointer += 1
            back_pointer -=1
