class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        toprow, bottomrow = 0, len(matrix) - 1

        while toprow <= bottomrow:
            middlerow = (toprow + bottomrow) // 2
            if matrix[middlerow][0] > target:
                bottomrow = middlerow - 1
            elif matrix[middlerow][-1] < target:
                toprow = middlerow + 1
            else:
                break
        
        if not (toprow <= bottomrow):
            return False
        
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            mid = (l + r) // 2
            if matrix[middlerow][mid] > target:
                r = mid - 1
            elif matrix[middlerow][mid] < target:
                l = mid + 1
            else:
                return True
        return False