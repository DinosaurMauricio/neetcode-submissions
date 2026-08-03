# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        

        def traverse(node):

            if node is None:
                return TreeNode(val)

            if val > node.val:
                node.right = traverse(node.right)

            elif val < node.val:
                node.left = traverse(node.left)
                    
            return node            

                        

        
        return traverse(root) 