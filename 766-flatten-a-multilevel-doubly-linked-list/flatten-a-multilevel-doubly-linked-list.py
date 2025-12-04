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
                    child_head = curr.child
                    child_tail = dfs(child_head)

                    curr.child = None
                    curr.next = child_head
                    child_head.prev = curr

                    if nextNode:
                        child_tail.next = nextNode
                        nextNode.prev = child_tail

                    last = child_tail
                    curr = nextNode
                else:
                    last = curr
                    curr = nextNode
            return last

        dfs(head)
        return head