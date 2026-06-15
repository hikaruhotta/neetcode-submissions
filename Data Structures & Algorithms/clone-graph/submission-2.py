"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.cache = {}
        return self.helper(node)

    def helper(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        if node in self.cache:
            return self.cache[node]
        
        clone_node = Node(node.val)
        self.cache[node] = clone_node

        clone_neighbors = [self.helper(neighbor) for neighbor in node.neighbors]
        clone_node.neighbors = clone_neighbors


        return clone_node