# O(mn) time | O(1) space
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        
        def capture(row, col):
            if (row < 0 or col < 0 or row == ROWS or col == COLS or board[row][col] != "O"):
                return
            board[row][col] = "Remain O"
            capture(row+1, col)
            capture(row-1, col)
            capture(row, col+1)
            capture(row, col-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                isBorderCell = r in [0, ROWS-1] or c in [0, COLS-1]
                if board[r][c] == "O" and isBorderCell:
                    capture(r,c)
        
        # turn everything that should not remain an O into a X
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "Remain O":
                    board[r][c] = "O"        
        