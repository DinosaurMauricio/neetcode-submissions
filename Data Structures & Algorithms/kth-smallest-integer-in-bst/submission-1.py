# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        count = 0
        res = 0

        def traverse(node):
            nonlocal count
            nonlocal res

            
            if not node:
                return 0

 
            

            c = traverse(node.left)
            count += 1
            if count == k:
                res = node.val

            c2 = traverse(node.right)

            

            return c+c2 + 1


        traverse(root)
        return res