# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #if not root:
        #    return []

        q = deque([root])
        res = []
        while q:
            #level = []
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            # this should be the MOST RIGHT node
            if node:
                res.append(node.val)

        return res