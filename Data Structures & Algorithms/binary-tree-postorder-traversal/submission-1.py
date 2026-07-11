# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        stack, visited = [root], [False]

        while stack:
            node, v = stack.pop(), visited.pop()
            if node:
                if v:
                    res.append(node.val)
                else:
                    stack.append(node)
                    visited.append(True)
                    stack.append(node.right)
                    visited.append(False)
                    stack.append(node.left)
                    visited.append(False)

        return res
        res = []
        def traverse(root):

            if not root:
                return 
            traverse(root.left)
            traverse(root.right)
            res.append(root.val)

        traverse(root)

        return res
        