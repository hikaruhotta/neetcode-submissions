# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse ll until slow node (exclusive)

        curr = head
        prev = None
        while curr and curr != slow:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        curr1, curr2 = prev, slow

        res = 0
        while curr2:
            res = max(res, curr1.val + curr2.val)
            curr1 = curr1.next
            curr2 = curr2.next
        return res



        
        