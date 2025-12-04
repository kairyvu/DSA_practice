"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        def dfs(currNode):
            node = currNode
            while node and not node.child:
                node = node.next
            if not node:
                return
            
            nextNode = node.next
            node.next = node.child
            node.child.prev = node
            node.child = None
            
            dfs(node.next)
            while node.next:
                node = node.next
            node.next = nextNode
            if nextNode:
                nextNode.prev = node
            dfs(nextNode)

        curr = head
        dfs(curr)
        return head
