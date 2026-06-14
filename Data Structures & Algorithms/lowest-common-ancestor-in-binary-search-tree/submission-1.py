# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.result = None
        self.helper(root, p, q)
        return self.result

    def helper(self, root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> None:
        if not root:
            return

        if p.val < q.val:
            small, large = p, q
        else:
            small, large = q, p
        
        if small.val <= root.val and root.val <= large.val:
            self.result = root
            return

        if root.val >= small.val and root.val >= large.val:
            self.helper(root.left, p, q)
        else:
            self.helper(root.right, p, q)
        
