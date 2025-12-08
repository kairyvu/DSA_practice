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
        curr = head
        while curr:
            copy = Node(curr.val, curr.next)
            curr.next = copy
            curr = copy.next
        
        curr = head
        while curr:
            copy = curr.next
            if curr.random:
                copy.random = curr.random.next
            curr = copy.next
        
        dummyHead = Node(0)
        dummyHead.next = head
        curr = dummyHead

        while curr and curr.next:
            curr.next = curr.next.next
            curr = curr.next
        return dummyHead.next