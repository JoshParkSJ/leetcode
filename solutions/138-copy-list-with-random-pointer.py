"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# O(n) time | O(n) space
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        
        hashCopy = {}
        hashReal = {}
        realToCopy = {}
        
        returnHead = copyNode = Node(head.val)
        hashCopy[hash(copyNode)] = copyNode
        hashReal[hash(head)] = head
        realToCopy[hash(head)] = hash(copyNode)
        node = head.next
        
        while node:
            copyNode.next = Node(node.val)
            copyNode = copyNode.next
            hashCopy[hash(copyNode)] = copyNode
            hashReal[hash(node)] = node
            realToCopy[hash(node)] = hash(copyNode)
            node = node.next
        
        node = head
        copyNode = returnHead
        while node:
            if node.random:
                realRandomHash = hashReal[hash(node.random)]
                copyRandomHash = realToCopy[hash(realRandomHash)]
                copyRandomNode = hashCopy[hash(copyRandomHash)]
                copyNode.random = copyRandomNode
            copyNode = copyNode.next
            node = node.next
        
        return returnHead
        
# ---------------
# cleaner solution
# instead of having 3 maps to convert real node to copy node, just use the node as key and copy node as reference

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':        
        if not head:
            return 
        cur, dic = head, {}
        # copy nodes
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        # copy random pointers
        while cur:
            if cur.random:
                dic[cur].random = dic[cur.random]
            if cur.next:
                dic[cur].next = dic[cur.next]
            cur = cur.next
        return dic[head]