# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        

        def traverse(node):

            if not node:
                return None

            
            nl = traverse(node.left)
            nr = traverse(node.right)

            if not nr:
                node.right = None
            
            if not nl:
                node.left = None


            # here we know its a leaf and its equal to the target
            # how can i remove it...
            if not nl and not nr and node.val == target:
                return None
            else:
                return node






        return traverse(root)