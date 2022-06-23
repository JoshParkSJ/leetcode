class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        [1,2,3],
        [4,5,6],
        [7,8,9]]
        ->
        [7,8,9],
        [4,5,6],
        [1,2,3]
        
        then

        [7,8,9],
        [4,5,6],
        [1,2,3]
        ->
        [7,4,1],
        [8,5,2],
        [9,6,3]
        """
        # flip up and down
        l = 0
        r = len(matrix) -1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1
        
        # flip left and right 
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
