# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxLength = 0
        self.helper(root)
        return self.maxLength
        
    def helper(self, root: Optional[TreeNode]) -> int:
        left = 1 + self.helper(root.left) if root.left else 0
        right = 1 + self.helper(root.right) if root.right else 0

        self.maxLength = max(self.maxLength, left + right)

        return max(left, right)




