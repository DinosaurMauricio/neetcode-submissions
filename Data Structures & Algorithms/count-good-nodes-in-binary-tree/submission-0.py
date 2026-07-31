# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0
        def traverse(node, max_value):
            nonlocal res
            if not node:
                return None

            if node.val >= max_value:
                res+=1
                max_value = node.val
                

            traverse(node.left, max_value)
            traverse(node.right,max_value)

        

        traverse(root, float('-inf'))
        return res

            