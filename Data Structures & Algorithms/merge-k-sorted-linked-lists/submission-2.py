# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for i, ls in enumerate(lists):
            if ls:
                heapq.heappush(min_heap, (ls.val, i))

        prevNode = ListNode(-100000)
        curr = prevNode
        
        while min_heap:
            (val, i) = heapq.heappop(min_heap)
            ls = lists[i]
            ls_next = ls.next
            lists[i] = ls_next
            if ls_next:
                heapq.heappush(min_heap, (ls_next.val, i))
            
            curr.next = ls
            curr = curr.next
        
        return prevNode.next

