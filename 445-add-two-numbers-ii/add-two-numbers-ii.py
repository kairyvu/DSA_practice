# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []
        
        while l1:
            stack1.append(l1)
            l1 = l1.next
        
        while l2:
            stack2.append(l2)
            l2 = l2.next
        
        extra = 0
        prevNode = None
        
        while stack1 or stack2 or extra:
            num1, num2 = 0, 0
            if stack1:
                num1 = stack1.pop().val
            if stack2:
                num2 = stack2.pop().val
            
            total = num1 + num2 + extra
            extra = total // 10
            newNode = ListNode(total % 10)
            newNode.next = prevNode
            prevNode = newNode

        return prevNode