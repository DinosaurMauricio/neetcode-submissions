# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def traverse(root):
            nonlocal res
            if not root:
                return 0

            val1 = traverse(root.left)
            val2 = traverse(root.right)

            res = max(res, val1 + val2)

            return max(val1,val2) + 1


        traverse(root)
        return res