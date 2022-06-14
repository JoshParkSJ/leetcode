# O(m+n) time | O(1) space
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for r in range(len(board)):
            colCounter = {}
            for c in range(len(board[0])):
                if board[r][c] != '.' and board[r][c] in colCounter:
                    return False
                colCounter[board[r][c]] = True
        
        for col in range(len(board[0])):
            rowCounter = {}
            for row in range(len(board)):
                if board[row][col] != '.' and board[row][col] in rowCounter:
                    return False
                rowCounter[board[row][col]] = True
                    
        for roww in range(3):
            for coll in range(3):
                x = roww*3
                y = coll*3
                boardCounter = {}
                
                for i in range(3):
                    for j in range(3):
                        if board[x+i][y+j] != '.' and board[x+i][y+j] in boardCounter:
                            return False
                        boardCounter[board[x+i][y+j]] = True

        return True