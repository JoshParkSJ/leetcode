# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time | O(n) space 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = []
        result = []
        self.traverse(root, 0, levels)
        for level in levels:
            result.append(level[-1])
        return result
    
    def traverse(self, node, level, levels):
        if not node:
            return
        if level == len(levels):
            levels.append([])
        levels[level].append(node.val)
        self.traverse(node.left, level+1, levels)
        self.traverse(node.right, level+1, levels)