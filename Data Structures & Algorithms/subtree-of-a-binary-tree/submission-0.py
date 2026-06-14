# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        # all nodes must match exploring
        if root.val == subRoot.val:
            left = self.isMatch(root.left, subRoot.left)
            right = self.isMatch(root.right, subRoot.right)
            if left and right:
                return True

        # otherwise traverwse deeper to find match
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isMatch(self, root1: Optional[TreeNode], root2: Optional[TreeNode]):
        if not root1 or not root2:
            return not root1 and not root2

        if root1.val != root2.val:
            return False

        return self.isMatch(root1.left, root2.left) and self.isMatch(root1.right, root2.right)