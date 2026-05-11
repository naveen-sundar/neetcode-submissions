# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(starting_node):
            if not starting_node:
                return
            res.append(starting_node.val)
            print(starting_node.val)
            dfs(starting_node.left)
            dfs(starting_node.right)
        dfs(root)
        return res