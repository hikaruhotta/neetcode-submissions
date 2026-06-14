# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.result = 0
        self.helper(root, -10000000)
        return self.result


    def helper(self, root: TreeNode, max_on_path: int) -> None:
        if not root:
            return None

        if root.val >= max_on_path:
            self.result += 1

        if root.left:
            self.helper(root.left, max(max_on_path, root.val))
        if root.right:
            self.helper(root.right, max(max_on_path, root.val))


        