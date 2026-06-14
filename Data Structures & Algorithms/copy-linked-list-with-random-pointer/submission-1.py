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
        nodes = {}
        prevNode = Node(-1)

        curr, copy_prev = head, prevNode

        while curr:
            if curr in nodes:
                curr_copy = nodes[curr]
            else:
                curr_copy = Node(curr.val)
                nodes[curr] = curr_copy
            
            copy_prev.next = curr_copy

            if curr.random:
                if curr.random in nodes:
                    random_copy = nodes[curr.random]
                else:
                    random_copy = Node(curr.random.val)
                    nodes[curr.random] = random_copy
        
                curr_copy.random = random_copy
            
            curr = curr.next
            copy_prev = copy_prev.next
        
        return prevNode.next
            
