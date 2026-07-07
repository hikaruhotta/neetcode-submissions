# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # found
            if root.left is None or root.right is None:
                if root.left is None and root.right is None:
                    return None
                elif root.left is None:
                    return root.right
                else:
                    return root.left
            else:
                # find smallest in right subtree and swap, then recursively call delete on swapped node
                curr = root.right
                while curr.left:
                    curr = curr.left
                root.val = curr.val
                root.right = self.deleteNode(root.right, root.val)
        
        return root
