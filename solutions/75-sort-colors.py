class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        red, white = [], []
        
        self.getColorIndex(nums, 0, red)
        left = self.sortColor(nums, red, left)
        
        self.getColorIndex(nums, 1, white)
        left = self.sortColor(nums, white, left)
        
    def getColorIndex(self, nums, color, colorArray):
        for idx, num in enumerate(nums):
            if num == color:
                colorArray.append(idx)
                
    def sortColor(self, nums, colorArray, left):
        start = left
        for i in colorArray:
            nums[start], nums[i] = nums[i], nums[start]
            start += 1
        return start