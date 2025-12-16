# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hsmap = {}
        for i, num in enumerate(inorder):
            hsmap[num] = i
        
        rootIndex = [0]
        def buildTree(left, right):
            if left > right:
                return None
            rootVal = preorder[rootIndex[0]]
            root = TreeNode(rootVal)
            rootIndex[0] += 1
            root.left = buildTree(left, hsmap[rootVal] - 1)
            root.right = buildTree(hsmap[rootVal] + 1, right)
            return root
        
        return buildTree(0, len(inorder) - 1)
