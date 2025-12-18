# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, nodeMax, nodeMin):
            if not node:
                return True
            if not nodeMin < node.val < nodeMax:
                return False
            return dfs(node.left, node.val, nodeMin) and dfs(node.right, nodeMax, node.val)

        return dfs(root, float("inf"), float("-inf"))