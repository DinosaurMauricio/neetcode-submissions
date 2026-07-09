# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack = []
        res = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            res.append(current.val)
            current = current.right

        return res

        res = []

        def traverse(root):
            if not root:
                return
            traverse(root.left)
            res.append(root.val)
            traverse(root.right)
            

        traverse(root)

        return res

        