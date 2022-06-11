# O(n) time | O(n) space where n is all the nodes in k linked lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # Linked lists don't work in heapify
        # Only lists or tuples (for tuples, the first value is compared)
        heap = [(linkedList.val, idx) for idx, linkedList in enumerate(lists) if linkedList]
        heapq.heapify(heap)
        head = curr = ListNode(None)
        while heap:
            val, idx = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            node = lists[idx] = lists[idx].next
            if node:
                # idx keeps track of which linked list it is in lists, 
                # not actual array idx
                heapq.heappush(heap, (node.val, idx))
        return head.next
        