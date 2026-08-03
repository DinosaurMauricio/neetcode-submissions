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
                v = traverse(node.right).val
                if  v == val:
                    node.right = TreeNode(val)

            elif val < node.val:
                v = traverse(node.left).val
                if  v == val:
                    node.left = TreeNode(val)
                    
            return node            

                        

        
        return traverse(root) 