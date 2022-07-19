# O(logn + k) time where logn is the height of tree | O(logn) space
# inorder traversal
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right

# ------------------------------------------------------------

# O(logn + k) time where logn is the height of tree | O(logn) space
# inorder traversal
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        
        while root:
            stack.append(root)
            root = root.left
        
        while k != 0:
            node = stack.pop()
            k -= 1
            if k == 0: return node.val
            node = node.right
            while node:
                stack.append(node)
                node = node.left
        
        return -1

