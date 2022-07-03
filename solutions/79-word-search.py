class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.backtrack(i, j, board, word, 0):
                    return True
        return False
    
    def backtrack(self, i, j, board, word, charIdx):
        if charIdx == len(word):
            return True
        if (i < 0 or i > len(board)-1 or
            j < 0 or j > len(board[0])-1 or
            board[i][j] != word[charIdx]):
            return
        
        board[i][j] = '#'
        if (self.backtrack(i+1, j, board, word, charIdx+1) or
            self.backtrack(i-1, j, board, word, charIdx+1) or
            self.backtrack(i, j+1, board, word, charIdx+1) or
            self.backtrack(i, j-1, board, word, charIdx+1)):
            return True
        
        board[i][j] = word[charIdx]

        
        
        