# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.result = True
        self.helper(root)
        return self.result
    
    def helper(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)

        if max(left, right) - min(left, right) > 1:
            self.result = False

        return 1 + max(left, right)