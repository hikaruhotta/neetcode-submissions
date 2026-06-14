# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        if count < k:
            return head

        prev, curr = None, head

        n = 0
        while curr and n < k:
            tmp_next = curr.next
            curr.next = prev
            prev = curr
            curr = tmp_next
            n += 1
        
        start, end, next = prev, head, curr

        if next:
            end.next = self.reverseKGroup(next, k)

        return start