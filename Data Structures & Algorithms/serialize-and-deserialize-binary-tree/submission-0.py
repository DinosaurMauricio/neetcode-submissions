# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        res = []
        def dfs(node):
            nonlocal res

            if not node:
                res.append("N")
                return 

            res.append(f"{node.val}")

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        array_data = data.split(",")
        index = 0

        def dfs():
            nonlocal index
            if  array_data[index] == "N":
                index+=1
                return

            node = TreeNode(int(array_data[index]))
            index+=1

            node.left = dfs()
            node.right = dfs()
            return node



        return dfs()
