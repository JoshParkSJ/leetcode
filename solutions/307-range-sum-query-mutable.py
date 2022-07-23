#Segment tree node
class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None
        
class NumArray(object):
    def __init__(self, nums):
        # O(n) time | O(n) space
        # sum of every level = n + n/2 + n/4 + ... + 1 = 2n space/time
        def createTree(nums, l, r):
            #base case
            if l > r:
                return None
                
            #leaf node
            if l == r:
                n = Node(l, r)
                n.total = nums[l]
                return n
            
            mid = (l + r) // 2            
            root = Node(l, r)
            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid+1, r)
            root.total = root.left.total + root.right.total
            return root
        
        self.root = createTree(nums, 0, len(nums)-1)
            
    def update(self, i, val):
        # O(logn) time | O(1) space
        def updateVal(root, i, val):
            # base case, value will be updated in a leaf, total is then propogated upwards
            if root.start == root.end:
                root.total = val
                return val
        
            mid = (root.start + root.end) // 2
            
            if i <= mid:
                updateVal(root.left, i, val) 
            else:
                updateVal(root.right, i, val)
            
            root.total = root.left.total + root.right.total
            return root.total
        
        return updateVal(self.root, i, val)

    def sumRange(self, i, j):
        # O(logn) time | O(1) space
        def rangeSum(root, i, j):
            # base case, we have the sum
            if root.start == i and root.end == j:
                return root.total
            
            mid = (root.start + root.end) // 2
            
            if j <= mid:
                # range is in left side
                return rangeSum(root.left, i, j)
            elif i >= mid + 1:
                # range is in right side
                return rangeSum(root.right, i, j)
            else:
                # range is before and after mid
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid+1, j)
        
        return rangeSum(self.root, i, j)
                
