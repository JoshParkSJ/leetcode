# O(mn) time | O(mn) space
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # find zero
        zeroes = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroes.append((i,j))
                    
        for zero in zeroes:
            self.setRowAndCol(zero[0], zero[1], matrix)
              
    def setRowAndCol(self, i, j, matrix):
        col = row = 0
        while col <= len(matrix[0])-1:
            matrix[i][col] = 0
            col += 1
        while row <= len(matrix)-1:
            matrix[row][j] = 0
            row += 1