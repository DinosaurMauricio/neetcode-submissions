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

            #print(node.val)
            if val > node.val:
                if traverse(node.right).val == val:
                    node.right = TreeNode(val)
                    return node

            elif val < node.val:
                if traverse(node.left).val == val:
                    node.left = TreeNode(val)
                    return node

            return node            

                        

        
        return traverse(root) 