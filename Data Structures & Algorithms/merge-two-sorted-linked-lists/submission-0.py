# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = list1, list2

        res = ListNode(0)
        traverse = res

        while cur1 and cur2:

            if cur1.val < cur2.val:
                traverse.next = cur1
                traverse = traverse.next
                cur1 = cur1.next
            else:
                traverse.next = cur2
                traverse = traverse.next
                cur2 = cur2.next
            
        while cur2:
            traverse.next = cur2
            traverse = traverse.next
            cur2 = cur2.next

        while cur1:
            traverse.next = cur1
            traverse = traverse.next
            cur1 = cur1.next

        return res.next
