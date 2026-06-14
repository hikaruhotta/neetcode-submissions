# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMinNode(self, root: TreeNode) -> TreeNode:
        curr = root

        while curr.left:
            curr = curr.left
        
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            if not root.left and not root.right:
                return None
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                min_node_right = self.findMinNode(root.right)
                root.val = min_node_right.val
                root.right = self.deleteNode(root.right, root.val)
                return root

                
            

        
        
        