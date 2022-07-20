# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    # O(n) time | O(n) space
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if node:
                result.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
            else:
                result.append('#')
        result = []
        dfs(root)
        return ' '.join(result)
 
    # O(n) time | O(n) space
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs():
            if nodes[0] == '#':
                nodes.popleft()
                return None
            
            node = TreeNode(int(nodes[0]))
            nodes.popleft()
            node.left = dfs()
            node.right = dfs()
            return node

        nodes = deque(data.split())
        return dfs()
                
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))