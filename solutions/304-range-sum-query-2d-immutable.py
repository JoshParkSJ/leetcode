class NumMatrix:

    # O(mn) time | O(mn) space
    def __init__(self, matrix: List[List[int]]):
        if matrix is None or not matrix:
            return
        n, m = len(matrix), len(matrix[0])
        self.sums = [ [0 for j in range(m+1)] for i in range(n+1) ]
        for i in range(1, n+1):
            for j in range(1, m+1):
                self.sums[i][j] = (matrix[i-1][j-1] + 
                                   self.sums[i][j-1] +
                                   self.sums[i-1][j] - 
                                   self.sums[i-1][j-1])

    # O(1) time
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        return (self.sums[row2][col2]
                - self.sums[row2][col1-1]
                - self.sums[row1-1][col2]
                + self.sums[row1-1][col1-1])

            


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# +-----+-+-------+     +--------+-----+     +-----+---------+     +-----+--------+
# |     | |       |     |        |     |     |     |         |     |     |        |
# |     | |       |     |        |     |     |     |         |     |     |        |
# +-----+-+       |     +--------+     |     |     |         |     +-----+        |
# |     | |       |  =  |              |  +  |     |         |  -  |              |
# +-----+-+       |     |              |     +-----+         |     |              |
# |               |     |              |     |               |     |              |
# |               |     |              |     |               |     |              |
# +---------------+     +--------------+     +---------------+     +--------------+

#    sums[i][j]      =    sums[i-1][j]    +     sums[i][j-1]    -   sums[i-1][j-1]   +  

#                         matrix[i-1][j-1]
        
        
# +---------------+   +---------+----+   +---+-----------+   +---------+----+   +---+---------
# |               |   |         |    |   |   |           |   |         |    |   |   |         
# |   (r1,c1)     |   |         |    |   |   |           |   |         |    |   |   |         
# |   +------+    |   |         |    |   |   |           |   +---------+    |   +---+         
# |   |      |    | = |         |    | - |   |           | - |      (r1,c2) | + |   (r1,c1)   
# |   |      |    |   |         |    |   |   |           |   |              |   |             
# |   +------+    |   +---------+    |   +---+           |   |              |   |             
# |        (r2,c2)|   |       (r2,c2)|   |   (r2,c1)     |   |              |   |             
# +---------------+   +--------------+   +---------------+   +--------------+   +-------------
