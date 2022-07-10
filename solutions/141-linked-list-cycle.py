# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# O(n) time | O(1) space
# this is just finding if there is a cycle
# if we want to return where the cycle begins, set slow or fast to head
# traverse 1 forward until they meet (where they meet is the start of cycle)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
            
        return False




