# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def validateSubtree(mNode, subNode):
            
            if not mNode and not subNode:
                return True
            
            if not mNode and subNode or  mNode and not subNode:
                return False
            
            if mNode.val != subNode.val:
                return False

            return validateSubtree(mNode.left, subNode.left) and validateSubtree(mNode.right, subNode.right)

        def traverse(node):

            if not node:
                return False

            res = False
            if subRoot.val == node.val:
                res =  validateSubtree(node, subRoot)
                
            return traverse(node.left) or traverse(node.right) or res
        
        return traverse(root)