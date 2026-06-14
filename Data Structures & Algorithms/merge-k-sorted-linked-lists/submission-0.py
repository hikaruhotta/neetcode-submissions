# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        
        result = lists[0]

        for i in range(1, len(lists)):
            result = self.mergeTwoLists(result, lists[i])
        
        return result
        

    def mergeTwoLists(self, list1, list2) -> Optional[ListNode]:
        prev_node = ListNode(-1)
        curr = prev_node
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        
        return prev_node.next


