# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.is_valid = True
        if root is None:
            return True
        self.helper(root)
        return self.is_valid

    def helper(self, root: TreeNode) -> tuple():
        if root.left is None and root.right is None:
            return (root.val, root.val)

        # max from left is smaller than val
        # min from right is greater than val

        if root.left:
            left_min, left_max = self.helper(root.left)
        else:
            left_min, left_max = None, None

        if root.right:
            right_min, right_max = self.helper(root.right)
        else:
            right_min, right_max = None, None
        
        if left_max and left_max >= root.val:
            self.is_valid = False
        if right_min and right_min <= root.val:
            self.is_valid = False
        
        vals = [left_min, left_max, right_min, right_max, root.val]
        vals = [val for val in vals if val is not None]
        return (min(vals), max(vals))


