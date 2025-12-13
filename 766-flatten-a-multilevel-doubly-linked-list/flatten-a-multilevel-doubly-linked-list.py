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
            curr = node
            last = node
            while curr:
                nextNode = curr.next
                if curr.child:
                    curr.next = curr.child
                    childTail = dfs(curr.child)
                    curr.child.prev = curr
                    curr.child = None

                    if nextNode:
                        childTail.next = nextNode
                        nextNode.prev = childTail
                    last = childTail
                    curr = nextNode
                else:
                    last = curr
                    curr = nextNode
            return last
        
        dfs(head)
        return head