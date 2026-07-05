"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        print(self.slice(grid))
        N = len(grid)

        if self.isLeaf(grid):
            return Node(grid[0][0], True, None, None, None, None)
        
        node = Node(grid[0][0], False, None, None, None, None)

        node.topLeft = self.construct([row[:N // 2] for row in grid[:N // 2]])
        node.topRight = self.construct([row[N // 2:] for row in grid[:N // 2]])
        node.bottomLeft = self.construct([row[:N // 2] for row in grid[N // 2:]])
        node.bottomRight = self.construct([row[N // 2:] for row in grid[N // 2:]])
        return node

        
    def isLeaf(self, grid: List[List[int]]) -> bool:
        val = grid[0][0]
        for row in range(len(grid)):
            for col in range(len(grid)):
                if grid[row][col] != val:
                    return False
        return True
    
    def slice(self, grid: List[List[int]]):
        N = len(grid)
        print([row[:N//2] for row in grid[:N//2]])



