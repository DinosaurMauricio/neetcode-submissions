# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                res.append(current.val)
                current = current.left
            
            current = stack.pop().right

        return res