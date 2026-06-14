# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True
        self.helper(root)
        return self.is_balanced

    def helper(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)

        if abs(left - right) > 1:
            self.is_balanced = False

        return max(left, right) + 1

    