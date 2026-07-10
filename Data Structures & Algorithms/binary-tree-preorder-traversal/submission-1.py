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

        while stack or current:
            while current:
                res.append(current.val)
                stack.append(current)
                current = current.left
                

            current = stack.pop().right
            #current = current.right
            

        return res


        res = []
        def traverse(root):

            if not root:
                return

            res.append(root.val)
            traverse(root.left)
            traverse(root.right)

        traverse(root)

        return res