class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []
        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][1]:
                newIndex, newVal = stack.pop()
                ans[newIndex] = i - newIndex
            stack.append([i, v])
        return ans