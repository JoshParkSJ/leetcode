# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time | O(logn) space
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.countDepth(root)
        
    def countDepth(self, node):
        if not node:
            return 0
        return max(1 + self.countDepth(node.right), 1 + self.countDepth(node.left))
        