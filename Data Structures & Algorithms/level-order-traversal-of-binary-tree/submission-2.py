# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            length = len(q)
            level = []
            for i in range(length):
                current = q.popleft()
                if current:
                    level.append(current.val)
                    q.append(current.left)
                    q.append(current.right)
            
            if level:
                res.append(level)

        return res