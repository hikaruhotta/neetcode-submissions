# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prevHead = ListNode(-1)
        prevHead.next = head

        slow, fast = prevHead, head
        # move fast pointer along n + 2 times
        for i in range(n):
            fast = fast.next

        # move slow and fast points along until fast is None. slow.next will be the Nth from End
        while fast:
            fast = fast.next
            slow = slow.next

        # slow,next = slow.next.next lol
        slow.next = slow.next.next

        return prevHead.next