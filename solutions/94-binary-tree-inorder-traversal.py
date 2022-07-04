# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time | O(logn) space
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.traverse(root, result)
        return result
    
    def traverse(self, node, result):
        if node:
            self.traverse(node.left, result)
            result.append(node.val)
            self.traverse(node.right, result)