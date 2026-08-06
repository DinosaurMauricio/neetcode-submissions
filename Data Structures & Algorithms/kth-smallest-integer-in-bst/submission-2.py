# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = []
        current = root
        count = 0
        
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            count+=1
            node = stack.pop()
            current = node.right
            
            if count == k:
                return node.val

        return 0

            
            

            
