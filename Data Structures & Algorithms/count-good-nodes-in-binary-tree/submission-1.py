# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # good means it's the maximum seen along the current path

        self.result = []
        self.helper(root, root.val)
        return len(self.result)
    
    def helper(self, root: TreeNode, max_path_val: int) -> None:
        if root is None:
            return
        
        if root.val >= max_path_val:
            self.result.append(root.val)
        
        if root.left:
            self.helper(root.left, max(max_path_val, root.val))
        if root.right:
            self.helper(root.right, max(max_path_val, root.val))
