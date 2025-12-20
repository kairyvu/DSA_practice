# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hsmap = defaultdict(list) # col: [(row, val)]

        q = deque([(root, 0)]) # (node, col)
        minCol = 0
        currRow = 0
        while q:
            for _ in range(len(q)):
                node, col = q.popleft()
                minCol = min(minCol, col)
                hsmap[col].append((currRow, node.val))
                if node.left:
                    q.append((node.left, col - 1))
                if node.right:
                    q.append((node.right, col + 1))
            currRow += 1
        
        res = []
        while hsmap[minCol]:
            res.append([])
            hsmap[minCol].sort()
            for _, num in hsmap[minCol]:
                res[-1].append(num)
            minCol += 1
        return res