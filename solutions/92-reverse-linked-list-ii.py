# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n) time | O(1) space
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if not head or left == right: 
            return head
        
        p = dummy = ListNode(None)
        dummy.next = head
        for i in range(left-1): 
            p = p.next
        tail = p.next

        for i in range(right-left):
            tmp = p.next                  # a)
            p.next = tail.next            # b)
            tail.next = tail.next.next    # c)
            p.next.next = tmp             # d)
        return dummy.next
    
    # dummy -> 1 -> 2 -> 3 -> 4 -> 5 a) temp = 2 b) 1->3 c) 2->4 d) 3->2
    # dummy -> 1 -> 3 -> 2 -> 4 -> 5
    # dummy -> 1 -> 4 -> 3 -> 2 -> 5