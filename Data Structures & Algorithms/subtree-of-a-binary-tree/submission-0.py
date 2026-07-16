# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def validateSub(p,q):

            if not p and not q:
                return True

            if not p or not q or p.val != q.val:
                #print("i think it arrives here")
                return False

            return validateSub(p.left,q.left) and validateSub(p.right,q.right)

        res = False
        def validate(root):
            nonlocal res

            if not root:
                return False

            if root.val == subRoot.val:

                if validateSub(root, subRoot):
                    res = True
                    return True


            validate(root.left)
            validate(root.right)

            return False

        validate(root)
        return res
