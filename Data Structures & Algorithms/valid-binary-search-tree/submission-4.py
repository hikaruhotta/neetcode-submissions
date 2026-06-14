# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        self.result = True
        self.helper(root)
        return self.result
        

    def helper(self, root: TreeNode) -> tuple(int, int):
        if not root.left and not root.right:
            return (root.val, root.val)

        vals = [root.val]
        
        if root.left:
            left_min, left_max = self.helper(root.left)
            if left_max >= root.val:
                self.result = False
            vals += [left_min, left_max]
        
        if root.right:
            right_min, right_max = self.helper(root.right)
            if right_min <= root.val:
                self.result = False
            
            vals += [right_min, right_max]
        
        return (min(vals), max(vals))
            