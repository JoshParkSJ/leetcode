
# O(n) time | O(n) space
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        def traverse(node, level):
            if not node:
                return
            if len(result) == level:
                result.append([])
            
            result[level].append(node.val)
            traverse(node.left, level+1)
            traverse(node.right, level+1)
            
        traverse(root, 0)
        return result[::-1]