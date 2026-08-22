# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        reverse = slow.next
        pre = None
        while reverse:
            temp = reverse.next
            reverse.next = pre
            pre = reverse
            reverse = temp

        slow.next = pre
        slow = slow.next

        while slow:
            #print(head.val, slow.val)
            if head.val != slow.val:
                return False

            slow = slow.next
            head = head.next

        return True