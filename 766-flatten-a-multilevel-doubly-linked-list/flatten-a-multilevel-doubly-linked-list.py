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
        if not head:
            return head
        
        def dfs(node):
            curr, prev = node, node
            while curr:
                nextNode = curr.next
                if curr.child:
                    childHead = curr.child
                    childTail = dfs(childHead)
                    curr.child = None
                    curr.next = childHead
                    childHead.prev = curr

                    if nextNode:
                        nextNode.prev = childTail
                        childTail.next = nextNode

                    prev = childTail
                    curr = nextNode
                else:
                    prev = curr
                    curr = nextNode
            return prev
        
        dfs(head)
        return head