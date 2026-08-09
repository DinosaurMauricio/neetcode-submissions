# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        previous = dummy
        current = head
        
        for _ in range(left - 1):
            previous = current
            current = current.next
    
        pre = None
        for _ in range(right - left + 1 ):
           # previous = previous.next
            temp = current.next
            current.next = pre
            pre = current
            current = temp

        previous.next.next = current
        previous.next = pre

        return dummy.next

        