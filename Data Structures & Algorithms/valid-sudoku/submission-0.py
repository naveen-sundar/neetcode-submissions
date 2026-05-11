class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9): # board[r][c] is a value from 1 to 9. In a given row, there should be no duplicates, we create 9 square tuples using math (see)
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in squares[(r//3, c//3)]:
                    return False
                else:
                    rows[r].add(board[r][c])
                    columns[c].add(board[r][c])
                    squares[(r // 3, c//3)].add(board[r][c])
        return True

    