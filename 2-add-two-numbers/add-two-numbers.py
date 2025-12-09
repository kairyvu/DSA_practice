# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        extra = 0
        head = ListNode()
        curr = head

        while l1 and l2:
            currSum = l1.val + l2.val + extra
            extra = 1 if currSum >= 10 else 0
            curr.next = ListNode(currSum % 10)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            currSum = l1.val + extra
            extra = 1 if currSum >= 10 else 0
            curr.next = ListNode(currSum % 10)
            curr = curr.next
            l1 = l1.next
        
        while l2:
            currSum = l2.val + extra
            extra = 1 if currSum >= 10 else 0
            curr.next = ListNode(currSum % 10)
            curr = curr.next
            l2 = l2.next
        
        if extra:
            curr.next = ListNode(extra)
            extra = 0
        
        return head.next