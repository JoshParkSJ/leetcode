# O(n!) time | O(n^2) space
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set() # (r+c) all the pos diagonals have the same r-c
        negDiag = set() # (r-c) all the neg diagonals have the same r-c
        
        result = []
        board = [["."]*n for _ in range(n)]
        
        def backtrack(row):
            if row == n:
                copy = ["".join(r) for r in board]
                result.append(copy)
            
            for col in range(n):
                if col in cols or row+col in posDiag or row-col in negDiag:
                    continue
                
                cols.add(col)
                posDiag.add(row+col)
                negDiag.add(row-col)
                board[row][col] = "Q"
                
                backtrack(row+1)
                
                # after finding a set or failing to find a set
                cols.remove(col)
                posDiag.remove(row+col)
                negDiag.remove(row-col)
                board[row][col] = "."

        backtrack(0)
        return result