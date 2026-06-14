"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
            original_to_copy = {}
            prev_head = Node(100000)
            copy_curr = prev_head

            curr = head
            while curr:
                # copy current node
                if curr in original_to_copy:
                    copy = original_to_copy[curr]
                else:
                    copy = Node(curr.val)
                    original_to_copy[curr] = copy

                copy_curr.next = copy
                copy_curr = copy
                
                # copy random node
                if curr.random:
                    if curr.random in original_to_copy:
                        random_copy = original_to_copy[curr.random]
                    else:
                        random_copy = Node(curr.random.val)
                        original_to_copy[curr.random] = random_copy
                    
                    copy.random = random_copy
                
                curr = curr.next
            
            return prev_head.next





