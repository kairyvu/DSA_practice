# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        n = 1
        curr = head
        while curr.next:
            n += 1
            curr = curr.next
        
        k %= n
        if k == 0:
            return head
        
        curr.next = head

        steps = n - k - 1
        newTail = head
        for _ in range(steps):
            newTail = newTail.next
        
        newHead = newTail.next
        newTail.next = None
        return newHead