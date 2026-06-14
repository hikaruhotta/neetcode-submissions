# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        val = preorder[0]
        node = TreeNode(preorder[0])
        left_len = inorder.index(val)


        left = self.buildTree(preorder[1: 1 + left_len], inorder[:left_len])
        right = self.buildTree(preorder[1 + left_len:], inorder[left_len + 1:])

        node.left = left
        node.right = right

        return node