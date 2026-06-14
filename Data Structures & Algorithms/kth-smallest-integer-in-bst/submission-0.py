# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = root.val
        self.counter = k
        self.helper(root)
        return self.result

    def helper(self, root: TreeNode):
        if not root:
            return

        self.helper(root.left)

        self.counter -= 1
        if self.counter == 0:
            self.result = root.val
            return
        
        if root.right:
            self.helper(root.right)


    