# O(n) time | O(logn) space bc we know for sure tree is balanced => tree height = logn 
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def createTree(left, right):
            if left > right:
                return None
            mid = (right + left) // 2
            node = TreeNode(nums[mid])
            node.left = createTree(left, mid-1)
            node.right = createTree(mid+1, right)
            return node
        
        return createTree(0, len(nums)-1)