# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """

        treeList = []
        def dfs(node):
            if not node:
                return None
            treeList.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(treeList)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        dataList = data.split(",")
        n = len(dataList)
        self.i = 0

        def dfs(low, high):
            if self.i == n:
                return None
            value = int(dataList[self.i])
            if not low < value < high:
                return None
            
            self.i += 1
            node = TreeNode(value)
            node.left = dfs(low, value)
            node.right = dfs(value, high)
            return node
        
        return dfs(float("-inf"), float("inf"))

        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans