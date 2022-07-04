# O(n) time | O(n) space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smallerThanX, greaterThanX = [], []
        smallerLL, greaterLL = None, None
        smallerHead, greaterHead = None, None
        
        while head:
            if head.val < x:
                smallerThanX.append(head)
            else:
                greaterThanX.append(head)
            head = head.next
        
        if smallerThanX:
            smallerLL = smallerThanX[0]
            smallerHead = smallerLL
            for i in range(1, len(smallerThanX)):
                smallerLL.next = smallerThanX[i]
                smallerLL = smallerLL.next
            
        if greaterThanX:
            greaterLL = greaterThanX[0]
            greaterHead = greaterLL
            for j in range(1, len(greaterThanX)):
                greaterLL.next = greaterThanX[j]
                greaterLL = greaterLL.next
            greaterLL.next = None
        
        if smallerLL:
            smallerLL.next = greaterHead
            return smallerHead
        elif greaterLL:
            return greaterHead
        else:
            return None

# ----------------------------------------
# same idea, no need to use aux array
# instead of aux array, just start a new thread of LL right off the bat


def partition(self, head, x):
    h1 = l1 = ListNode(0)
    h2 = l2 = ListNode(0)
    while head:
        if head.val < x:
            l1.next = head
            l1 = l1.next
        else:
            l2.next = head
            l2 = l2.next
        head = head.next
    l2.next = None
    l1.next = h2.next
    return h1.next