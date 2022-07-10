# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# O(n) time | O(1) space
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        cycleExists = False
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                cycleExists = True
                break
        
        if not cycleExists: return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow
        