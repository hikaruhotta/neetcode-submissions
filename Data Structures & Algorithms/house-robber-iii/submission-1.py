# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        self.cache = {}
        return self.helper(root, True)
    
    def helper(self, root: Optional[TreeNode], canRob: bool) -> int:
        if not root:
            return 0

        if (root, canRob) in self.cache:
            return self.cache[(root, canRob)]

        candidates = []
        
        # Option 1: Rob
        if canRob:
            candidates.append(root.val + self.helper(root.left, False) + self.helper(root.right, False))

        # Option 2: Do not rob
        candidates.append(self.helper(root.left, True) + self.helper(root.right, True))

        result = max(candidates)
        self.cache[(root, canRob)] = result
        return result

