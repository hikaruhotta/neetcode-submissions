# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.helper(root)
        return self.result


    def helper(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left, right = self.helper(root.left), self.helper(root.right)

        self.result = max(self.result, left, right, left + right)

        return 1 + max(left, right)
