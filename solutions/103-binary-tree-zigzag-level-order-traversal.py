# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time | O(w) space where w is the max width of a level
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        result = []
        queue = collections.deque([(root,0)])
        while queue:
            curr, level = queue.popleft()
            if len(result) == level:
                result.append([])
            
            result[level].append(curr.val)
            if curr.left:
                queue.append((curr.left, level+1))
            if curr.right:
                queue.append((curr.right, level+1))
        
        for idx, level in enumerate(result):
            if idx % 2 == 1:
                result[idx] = level[::-1]
        return result