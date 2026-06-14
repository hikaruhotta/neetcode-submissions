# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # empty list handling
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        l1_head, l2_head = l1, l2
        l1_length, l2_length = self.getLength(l1), self.getLength(l2)
        
        carry = 0
        prev_l1, prev_l2 = None, None
        while l1 and l2:
            total = l1.val + l2.val + carry
            carry = 0
            if total >= 10:
                carry = 1
            l1.val = total % 10
            l2.val = total % 10

            prev_l1, prev_l2 = l1, l2

            l1 = l1.next
            l2 = l2.next

        if l1 or l2:
            if l1_length > l2_length:
                while l1:
                    total = l1.val + carry
                    carry = 0
                    if total >= 10:
                        carry = 1
                    l1.val = total % 10
                    prev_l1 = l1
                    l1 = l1.next

                if carry == 1:
                    prev_l1.next = ListNode(1)

                return l1_head
            else:
                while l2:
                    total = l2.val + carry
                    carry = 0
                    if total >= 10:
                        carry = 1
                    l2.val = total % 10
                    prev_l2 = l2
                    l2 = l2.next

                if carry == 1:
                    prev_l2.next = ListNode(1)

                return l2_head

        else:
            if carry == 1:
                prev_l1.next = ListNode(1)
            
            return l1_head
        
            


    def getLength(self, l1: ListNode):
        count = 0
        curr = l1
        while curr:
            count += 1
            curr = curr.next
        return count