# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res = 0
        val = 0
        def traverse(root):
            nonlocal res
            nonlocal val

            if not root:
                return

            traverse(root.left)
            val+=1
            if val == k:
                res = root.val
            traverse(root.right)

        traverse(root)
            
        return res

        