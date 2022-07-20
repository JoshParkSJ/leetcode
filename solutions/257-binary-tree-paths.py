# recursive
# O(n) time | O(logn) space
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        stack = []
        self.dfs(root, res, [])
        for idx, path in enumerate(res):
            res[idx] = "->".join(path)
        return res
    
    def dfs(self, node, res, curr):
        if not node:
            return
        if not node.left and not node.right:
            res.append(curr + [str(node.val)])
            return
        
        curr += [str(node.val)]
        self.dfs(node.left, res, curr)
        self.dfs(node.right, res, curr)
        curr.pop()
        
# -----------------------------
# iterative
# O(n) time | O(n) space
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root: return []
        res = []
        stack = [(root, str(root.val))]
        
        while stack:
            node, path = stack.pop()
            
            if not node.left and not node.right:
                res.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))
        
        return res