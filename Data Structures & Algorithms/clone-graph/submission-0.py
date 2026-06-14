"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        self.original_to_copy = {}
        return self.helper(node)

    def helper(self, node: 'Node'):
        if node in self.original_to_copy:
            return self.original_to_copy[node]

        copy_node = Node(node.val)
        self.original_to_copy[node] = copy_node
        
        neighbor_copies = []
        for neighbor in node.neighbors:
            neighbor_copy = self.helper(neighbor)
            neighbor_copies.append(neighbor_copy)

        self.original_to_copy[node].neighbors = neighbor_copies
        
        return copy_node
       
            
                



