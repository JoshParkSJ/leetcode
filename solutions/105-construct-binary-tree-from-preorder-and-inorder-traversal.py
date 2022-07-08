# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# pre-order: 0th index is always the root (for every recursion)
# in-order: find the root index, anything to the left is the left subtree 
# O(n^2) time | O(n^2) space
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        # O(n) time for indexing
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        
        # O(logn) average case | O(n) worst case <= space
        # O(n) space for array
        # O(n) time for splicing
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root
    

# -----------------------------------------------------------

# inorder: [4,2,5,1,6,3,7]
# preorder: [1,2,4,5,3,6,7]
# as we pop off left from pre-order

#        1           [2,4,5,3,6,7]
#     2              [4,5,3,6,7]
#   4                [5,3,6,7]

#        1
#     2
#   4  5            [3,6,7]


#        1
#     2     3
#   4  5            [6,7]  <- we can build in preorder order, but using inorder to keep track of where is left/right subtree


# O(n) time | O(n) space
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # O(n) space | O(n) time
        inorderLookup = { value: index for index, value in enumerate(inorder) }
        preorder = deque(preorder)
        
        # O(logn) recursion stack space
        # O(n) time
        def recurse(start, end):
            if start > end:
                return None
            else:
                valToAdd = preorder.popleft()
                root = TreeNode(valToAdd)
                mid = inorderLookup[valToAdd]
                
                root.left = recurse(start, mid-1)
                root.right = recurse(mid+1, end)
                
                return root
        
        return recurse(0, len(preorder)-1)
            