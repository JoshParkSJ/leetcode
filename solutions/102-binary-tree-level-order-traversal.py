# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time | O(w) space where w is the max width of the level
# we don't include input and output space in space complexity

# DFS recursive
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.dfs(root, 0, res)
        return res
        
    def dfs(self, root, level, res):
        if not root:
            return 
        if len(res) == level:
            res.append([])
        res[level].append(root.val)
        self.dfs(root.left, level+1, res)
        self.dfs(root.right, level+1, res)

# DFS iterative
class Solution:
    res, stack = [], [(root, 0)]
    while stack:
        curr, level = stack.pop()
        if curr:
            if len(res) == level:
                res.append([])
            res[level].append(curr.val)
            stack.append((curr.right, level+1))
            stack.append((curr.left, level+1))
    return res

# BFS iterative
def levelOrder(self, root):
    from collections import deque
    res, queue = [], deque([(root, 0)])
    while queue:
        curr, level = queue.popleft()
        if curr:
            if len(res) == level:
                res.append([])
            res[level].append(curr.val)
            queue.append((curr.left, level+1))
            queue.append((curr.right, level+1))
    return res
