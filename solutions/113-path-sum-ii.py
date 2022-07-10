# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time | O(n) worst space or O(logn) avg space
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        self.getPathSum(root, targetSum, [], result)
        return result
    
    def getPathSum(self, node, targetSum, path, result):
        if not node:
            return
        
        targetSum -= node.val
        if not node.left and not node.right and targetSum == 0:
            path.append(node.val)
            result.append(path)
            return
        
        self.getPathSum(node.left, targetSum, path+[node.val], result)
        self.getPathSum(node.right, targetSum, path+[node.val], result)