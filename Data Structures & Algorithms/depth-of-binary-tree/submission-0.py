# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        res = 1
        
        # count the children
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        # take the max between the two
        res += max(left, right)
        
        return res

        