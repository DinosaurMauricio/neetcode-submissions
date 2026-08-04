# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0
        current = head
        while current:
            length+=1
            current = current.next

        if length <= n:
            return head.next
        
        current = head
        for _ in range(length - n - 1):
            current = current.next

        temp = current.next
        current.next = temp.next

        return head