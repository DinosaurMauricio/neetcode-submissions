# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        res = True
        def traverse(node):
            nonlocal res
            if not node:
                return 0

            val = traverse(node.left)
            val2 = traverse(node.right)


            if val2-val not in [0,1,-1]:
                res =False

            return max(val,val2) +1


        traverse(root)

        return res