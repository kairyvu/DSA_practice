# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levelOrder = {}
        q = deque([(root, 0)])
        minOrder = 0

        while q:
            node, order = q.popleft()
            if order not in levelOrder:
                levelOrder[order] = []
            levelOrder[order].append(node.val)
            if node.left:
                q.append((node.left, order - 1))
                minOrder = min(minOrder, order - 1)
            if node.right:
                q.append((node.right, order + 1))
        
        currOrder = minOrder
        res = []
        while currOrder in levelOrder:
            res.append(levelOrder[currOrder])
            currOrder += 1
        return res