# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(nlogn) time | O(logn) space for recursion stack
class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head    # return head in case there's only 1 node
        
        mid = self.getMid(head)  

        start = mid.next   # right sub LL
        mid.next = None    # left sub LL
        l, r = self.sortList(head), self.sortList(start)
        return self.merge(l, r)
    
    # get mid node (memorize this, useful for other LL questions)
    # if you're not convinced, try it on 3 nodes and 4 nodes
    def getMid(self, head):
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def merge(self, left, right):
        tail = dummy = ListNode()
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        if left:
            tail.next = left
        if right:
            tail.next = right
        
        return dummy.next