# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def traverse(node):
            if not node:
                return None

            if key < node.val:
                node.left = traverse(node.left)
            elif key > node.val:
                node.right = traverse(node.right)
            else:
                # we know key == node value
                if node.right:

                    replace = node.right
                    while replace.left:
                        replace = replace.left

                    temp = node.left 
                    node = node.right
                    replace.left = temp
                    
                    
                    return node
                elif node.left:
                    temp = node.right
                    node = node.left
                    node.right = temp
                else:
                    return None
                
                return node
        
            return node
            
        return traverse(root)