# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time | O(n) space
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float("-inf"), float("inf"))
    
    def validate(self, node, minVal, maxVal):
        if not node:
            return True
        
        if node.val <= minVal or node.val >= maxVal:
            return False
        
        return (self.validate(node.left, minVal, node.val) and 
                self.validate(node.right, node.val, maxVal))
    