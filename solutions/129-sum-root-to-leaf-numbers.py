# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time | O(logn) space
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        numbers = []
        self.getNumbers(root, "", numbers)
        return sum(numbers)
    
    def getNumbers(self, node, path, numbers):
        if not node:
            return
        if not node.left and not node.right:
            numbers.append(int(path + str(node.val)))
            return
        
        self.getNumbers(node.left, path + str(node.val), numbers)
        self.getNumbers(node.right, path + str(node.val), numbers)
            
        