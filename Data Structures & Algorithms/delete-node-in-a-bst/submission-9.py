# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def traverse(node, key):
            if not node:
                return None
            
            if key < node.val:
                node.left = traverse(node.left, key)
            elif key > node.val:
                node.right = traverse(node.right, key)
            else:
                # found the value to remove
                if not node.left and not node.right:
                    return None
                
                if node.right:
                    temp = node.left

                    replace = node.right
                    while replace.left:
                        replace = replace.left
                    node = node.right
                    replace.left = temp
                else:
                    temp = node.right
                    node = node.left
                    node.right = temp

                return node
            return node

        return traverse(root, key)
