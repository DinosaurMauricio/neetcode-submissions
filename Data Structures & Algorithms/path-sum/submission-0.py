# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def traverse(node, totalSum):

            if not node:
                return False

            totalSum += node.val
            if not node.left and not node.right and totalSum == targetSum:
                return True

            return traverse(node.left, totalSum) or traverse(node.right, totalSum)
        return traverse(root, 0)