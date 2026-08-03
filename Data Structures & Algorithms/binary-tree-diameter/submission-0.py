# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        max_diameter = 0
        def traverse(node):
            nonlocal max_diameter
            if node is None:
                return 0

            h_left = traverse(node.left)
            h_right = traverse(node.right)

            h = max(h_left, h_right)

            max_diameter = max(max_diameter, h_left + h_right)

            return h + 1


        traverse(root)
        return max_diameter