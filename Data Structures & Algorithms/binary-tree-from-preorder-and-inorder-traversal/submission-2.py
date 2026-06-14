# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        
        root = preorder[0]
        inorder_pivot = inorder.index(root)

        root = TreeNode(root)

        inorder_left = inorder[:inorder_pivot]
        inorder_right = inorder[inorder_pivot + 1:]

        preorder_left = preorder[1 : 1 + len(inorder_left)]
        preorder_right = preorder[1 + len(inorder_left):]

        left = self.buildTree(preorder_left, inorder_left)
        right = self.buildTree(preorder_right, inorder_right)

        root.left = left
        root.right = right

        return root

