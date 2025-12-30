# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        
        def addRow(node):
            left = node.left
            right = node.right
            newLeft, newRight = TreeNode(val), TreeNode(val)
            newLeft.left = left
            newRight.right = right
            node.left = newLeft
            node.right = newRight


        q = deque([root])
        currDepth = 1
        
        while q and currDepth < depth - 1:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            currDepth += 1
        
        while q:
            node = q.popleft()
            addRow(node)
        return root