class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0

        i = 0
        j = len(height)-1
        max_vol = 0
        while i < j:
            height_calc = height[i] if height[j] > height[i] else height[j]
            vol = (j - i) * height_calc
            if vol > max_vol:
                max_vol = vol 
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_vol

            



        