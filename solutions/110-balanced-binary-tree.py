
# bottom up recursion
# O(n) time | O(n) space
# if recursive calls before conditional check, then its bottom up. If recursive call after conditional check, its top down
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.checkBalance(root)[0]
    
    def checkBalance(self, node):
        if not node:
            return (True, 0)
        
        left, right = self.checkBalance(node.left), self.checkBalance(node.right)
        
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        
        return (balanced, max(left[1], right[1]) + 1)
        