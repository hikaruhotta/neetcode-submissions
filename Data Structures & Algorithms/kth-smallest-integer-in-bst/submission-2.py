# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k - 1
        self.result = None
        self.helper(root)
        return self.result
        
    def helper(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        self.helper(root.left)

        if self.k > 0:
            self.k -= 1
        elif self.k == 0:
            self.result = root.val
            self.k -= 1

        self.helper(root.right)