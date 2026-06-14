# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        level = [root]

        while level:
            next_level = []
            sub_result = []
            for node in level:
                if node:
                    sub_result.append(node.val)
                    next_level.append(node.left)
                    next_level.append(node.right)
            level = next_level
            if len(sub_result) > 0:
                result.append(sub_result)
        
        return result



