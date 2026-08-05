# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def traverse(root):
            nonlocal res
            if not root:
                return 0

        
            val = traverse(root.left)
            val2 = traverse(root.right)

            if abs(val - val2) > 1:
                res = False

            return max(val,val2) + 1
        
        traverse(root)
        return res