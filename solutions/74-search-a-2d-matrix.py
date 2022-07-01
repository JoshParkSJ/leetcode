# O(logn + logm) time | O(1) space
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 1:
            if len(matrix[0]) == 1:
                return matrix[0][0] == target
            return self.targetIsInCurrRow(matrix[0], target)
        
        top, bottom = 0, len(matrix)-1
        while top <= bottom:
            mid = (top + bottom) // 2
            
            if target > matrix[mid][0]:
                top = mid+1
                if self.targetIsInCurrRow(matrix[mid], target):
                    return True
            elif target < matrix[mid][0]:
                bottom = mid-1
                if self.targetIsInCurrRow(matrix[mid], target):
                    return True
            else:
                return True
        return False
    
    def targetIsInCurrRow(self, currRow, target):
        left, right = 0, len(currRow)-1
        if currRow[0] <= target <= currRow[-1]:
            while left <= right:
                mid = (left + right) // 2
                if target > currRow[mid]:
                    left = mid+1
                elif target < currRow[mid]:
                    right = mid-1
                else:
                    return True
        return currRow[left] == target