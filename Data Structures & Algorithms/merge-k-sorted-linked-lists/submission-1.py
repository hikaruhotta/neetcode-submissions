# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        prev_node = ListNode(-1)
        curr = prev_node

        while sum([1 for node in lists if node]) > 0:
            min_index = None

            for i, node in enumerate(lists):
                if node:
                    if min_index is None:
                        min_index = i
                    elif lists[min_index].val > node.val:
                        min_index = i
            
            assert(min_index is not None)

            curr.next = lists[min_index]
            lists[min_index] = lists[min_index].next
            curr = curr.next
        
        return prev_node.next