# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def traverse(node, node2):

            if not node and not node2:
                return None

            if node and node2:
                node.val += node2.val
        
            if not node2:
                return node

            if not node:
                return node2

            node.left = traverse(node.left, node2.left)
            node.right = traverse(node.right, node2.right)

            return node
            
            

        return traverse(root1, root2)