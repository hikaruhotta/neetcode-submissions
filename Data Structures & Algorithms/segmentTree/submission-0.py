class Node:
    def __init__(self, total: int, L: int, R: int):
        self.total, self.L, self.R = total, L, R
        self.left, self.right = None, None

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.root = self.build(0, len(nums) - 1)

    def build(self, L: int, R: int) -> Node:
        if L == R:
            return Node(self.nums[L], L, R)
        
        M = (L + R) // 2

        node = Node(0, L, R)

        left, right = self.build(L, M), self.build(M + 1, R)
        node.left, node.right = left, right
        node.total = node.left.total + node.right.total

        return node

    
    def update(self, index: int, val: int) -> None:
        self.updateHelper(index, val, self.root)
    
    def updateHelper(self, index: int, val: int, node: Node) -> None:
        if node.L == node.R:
            node.total = val
            return
        
        M = (node.L + node.R) // 2

        if index <= M:
            self.updateHelper(index, val, node.left)
        else:
            self.updateHelper(index, val, node.right)
        node.total = node.left.total + node.right.total

    
    def query(self, L: int, R: int) -> int:
        return self.queryHelper(L, R, self.root)

    def queryHelper(self, L: int, R: int, node: Node) -> int:
        if L == node.L and R == node.R:
            return node.total
        
        M = (node.L + node.R) // 2

        if R <= M:
            return self.queryHelper(L, R, node.left)
        elif L > M:
            return self.queryHelper(L, R, node.right)
        else:
            return self.queryHelper(L, M, node.left) + self.queryHelper(M + 1, R, node.right)


