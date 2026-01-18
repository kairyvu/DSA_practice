# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        treeList = []
        def dfs(node):
            if not node:
                treeList.append("N")
                return
            treeList.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(treeList)        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        dataList = data.split(",")
        self.i = 0
        
        def dfs():
            if dataList[self.i] == "N":
                self.i += 1
                return None
            newNode = TreeNode(int(dataList[self.i]))
            self.i += 1
            newNode.left = dfs()
            newNode.right = dfs()
            return newNode
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))