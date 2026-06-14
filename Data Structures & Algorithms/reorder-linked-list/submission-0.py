# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid, end = slow, fast

        curr = mid.next
        second = None
        mid.next = None

        while curr:
            tmp = curr.next
            curr.next = second
            second = curr
            curr = tmp

        first = head

        while first and second:
            tmp_first, tmp_second = first.next, second.next

            first.next = second
            second.next = tmp_first

            first = tmp_first
            second = tmp_second
        

    def printLinkedList(self, head):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        print(vals)

        