class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0) # least recently used
        self.tail = Node(0, 0) # recently used
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.remove(self.dic[key])
        n = Node(key, value)
        self.add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self.remove(n)
            del self.dic[n.key]

    # helper
    def remove(self, node):
        # 1 <-> 2 <-> 3
        prev = node.prev
        nextt = node.next
        prev.next = nextt
        nextt.prev = prev
        # 1 <-------> 3

    # helper
    def add(self, node):
        # 1 <-> 2 <-> 3
        prev = self.tail.prev 
        prev.next = node
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail
        # head (none) <-> 1 <-> 2 <-> n <-> tail (none)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)