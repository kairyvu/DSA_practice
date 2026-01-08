# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        INT_LIMIT = 10**9 + 7

        def getTotal(node):
            if not node:
                return 0
            return node.val + getTotal(node.left) + getTotal(node.right)
        
        total = getTotal(root)
        self.minProduct = 0

        def getTreeProduct(node):
            if not node:
                return 0
            currSubTreeSum = node.val + getTreeProduct(node.left) + getTreeProduct(node.right)
            currProduct = (total - currSubTreeSum) * currSubTreeSum
            self.minProduct = max(self.minProduct, currProduct)
            return currSubTreeSum

        getTreeProduct(root)
        return self.minProduct % INT_LIMIT