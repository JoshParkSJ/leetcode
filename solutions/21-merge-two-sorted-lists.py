# O(m + n) time | O(m + n) space
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode(0)
        
        while l1 and l2:
            if l1.val > l2.val:
                node.next = ListNode(l2.val)
                l2 = l2.next
            else:
                node.next = ListNode(l1.val)
                l1 = l1.next
            node = node.next
        node.next = l1 or l2
        return dummy.next