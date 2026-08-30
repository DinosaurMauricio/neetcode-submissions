# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        

        traverseA = headA
        while traverseA:
            traverseB = headB

            while traverseB:
                if traverseA == traverseB:
                    return traverseA
                traverseB = traverseB.next
            traverseA = traverseA.next

        

        return None