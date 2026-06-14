# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = None
        self.k = k
        self.inOrderTraversal(root)
        return self.res

    def inOrderTraversal(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        
        self.inOrderTraversal(root.left)

        self.k -= 1

        if self.k == 0:
            self.res = root.val
            return
        
        self.inOrderTraversal(root.right)




            
        




    