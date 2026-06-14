# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow, fast = head, head.next

        while slow != fast and fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow == fast
        
