"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hsmap = {}
        dummyHead = Node(-1)
        currNode = dummyHead

        while head:
            val, next = head.val, head.next
            newNode = Node(val)
            currNode.next = newNode
            currNode = currNode.next
            hsmap[head] = newNode
            head = head.next
            
        for node in hsmap:
            oldRandomNode = node.random
            if not oldRandomNode:
                continue
            newRandomNode = hsmap[oldRandomNode]
            hsmap[node].random = newRandomNode

        return dummyHead.next