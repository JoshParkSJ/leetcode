# O(logn) time or O(n) worst case | O(1) space
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val > max(q.val, p.val):
                root = root.left
            elif root.val < min(q.val, p.val):
                root = root.right
            else:
                return root