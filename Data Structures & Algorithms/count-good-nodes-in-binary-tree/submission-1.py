# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def traverse(node, max_value):
            res = 0
            if not node:
                return res

            if node.val >= max_value:
                res = 1
                max_value = node.val
                

            return traverse(node.left, max_value) + traverse(node.right,max_value) + res

        return traverse(root, float('-inf'))

            