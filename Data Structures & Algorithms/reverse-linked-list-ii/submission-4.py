# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prevNode = ListNode(-1)
        prevNode.next = head
        
        prev = prevNode
        curr = head
        
        for i in range(left - 1):
            prev = curr
            curr = curr.next
        
        reversePrev = prev
        reverseStart = curr

        reverseNext = head
        for i in range(right):
            reverseNext = reverseNext.next

        for i in range(right - left + 1):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        reversePrev.next = prev
        reverseStart.next = reverseNext

        return prevNode.next

        
        

        
        
