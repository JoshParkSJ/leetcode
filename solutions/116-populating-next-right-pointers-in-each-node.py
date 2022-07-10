
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# O(n) time | O(n) space
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque([(root, 0)])
        levels = []
        while queue:
            curr, level = queue.popleft()
            if curr:
                if len(levels) == level:
                    levels.append([])
                    levels[level].append(curr)
                    curr.next = None
                else:
                    curr.next = levels[level].pop()
                    levels[level].append(curr)

                queue.append((curr.right, level+1))
                queue.append((curr.left, level+1))

        return root


# ------------------------------------------------

# O(n) time | O(logn) space for recursion stack
# a true BFS
class Solution:
    def connect(self, root):
        if not root: return None
        q = deque([root])
        while q:
            rightNode = None
            for _ in range(len(q)): # traverse through nodes in level
                cur = q.popleft()
                cur.next, rightNode = rightNode, cur
                if cur.right:
                    q.extend([cur.right, cur.left]) # all nodes in a level are present in the queue rn because
                                                    # every forloop goes through all levels and loads all l/r child into queue
        return root


# -----------------------------------------

# O(n) time | O(1) space
class Solution:
    def connect(self, root):
        head = root
        while root:
            cur, root = root, root.left
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                    if cur.next: cur.right.next = cur.next.left
                else: break
                cur = cur.next
                
        return head
