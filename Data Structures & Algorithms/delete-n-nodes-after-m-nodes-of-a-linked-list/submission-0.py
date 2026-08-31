# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        
        trav = head
        c1, c2 = m, n 

        while trav:
           # print(c1)
            if c1  > 1:
                trav = trav.next
                c1-=1
            else:
                #print("here")
                temp = trav.next
                while temp and c2 > 0:
                    temp = temp.next
                    c2-=1
                
                trav.next = temp
                trav = trav.next
                c1, c2 = m,n 
        return head