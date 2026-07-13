# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:


        #max_result = 0
        def traverse(root, val):
            if not root:
                return val

            op1 = traverse(root.left, val + 1)
            op2 = traverse(root.right, val + 1)

            return  max(op1,op2)

        res = traverse(root, 0)

        return res

    
        
        