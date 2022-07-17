# O(n+m) time | O(n+m) space for recursion stack
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numOfIslands = 0
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == "1":
                    self.searchIslands(grid, i, j, visited)
                    numOfIslands += 1
        
        return numOfIslands
    
    def searchIslands(self, grid, row, col, visited):
        if row > len(grid)-1 or row < 0 or col > len(grid[0])-1 or col < 0 or (row,col) in visited or grid[row][col] == "0":
            return
        visited.add((row,col))
        self.searchIslands(grid, row+1, col, visited)
        self.searchIslands(grid, row-1, col, visited)
        self.searchIslands(grid, row, col+1, visited)
        self.searchIslands(grid, row, col-1, visited)