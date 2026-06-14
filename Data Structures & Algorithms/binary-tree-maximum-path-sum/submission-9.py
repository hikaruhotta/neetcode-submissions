# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.result = -float('inf')
        self.helper(root)
        return self.result
    
    def helper(self, root: TreeNode) -> int:
        left, right = 0, 0
        if root.left:
            left = self.helper(root.left)
        if root.right:
            right = self.helper(root.right)

        self.result = max(self.result, root.val, left + root.val, right + root.val, left + right + root.val)

        return max(root.val, root.val + left, root.val + right)