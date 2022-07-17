#O(n) time | O(n) space
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dictA = set()
        while headA:
            dictA.add(headA)
            headA = headA.next
        
        while headB:
            if headB in dictA:
                return headB
            headB = headB.next
        return None

# ----------------------------------


# O(n) time | O(1) space
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pA = headA
        pB = headB

        while pA != pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next

        return pA

# say pA is 3 nodes longer than pB
# once pB reaches the end, set pB to start of pA linked list
# when pA finally reaches the end, pB is at the same position as pA in parallel
# move forward together in parallel positions until they are the same node

# alternatively, we can just find the difference in length and traverse forward the extra for the longer LL