# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle node of list with slow and fast pointers
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        middle = slow

        # reverse list from slow.next
        prev, curr = None, middle.next
        while curr:
            tmp_next = curr.next
            curr.next = prev
            prev = curr
            curr = tmp_next
        reverse_start = prev

        # split into two lists
        middle.next = None

        # interleaving time!
        list1, list2 = head, reverse_start

        prevNode = ListNode(-1)
        curr = prevNode

        odd = True
        while list1 and list2:
            if odd:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
            odd = not odd
        
        if list1:
            curr.next = list1
        
        head = prevNode.next

