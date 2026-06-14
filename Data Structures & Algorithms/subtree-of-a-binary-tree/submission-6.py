# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if subRoot is None:
            return True
        
        if self.isSameTree(root, subRoot):
            return True
        
        left, right = self.isSubtree(root.left, subRoot), self.isSubtree(root.right, subRoot)
        return left or right


    def isSameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return root1 == root2
        
        if root1.val != root2.val:
            return False
        
        left, right = self.isSameTree(root1.left, root2.left), self.isSameTree(root1.right, root2.right)
        return left and right
        
