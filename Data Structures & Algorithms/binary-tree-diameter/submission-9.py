# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0

        def count(root):
            nonlocal res

            if not root:
                return 0

            left = count(root.left)
            right = count(root.right)
            curr = left + right

            res = max(curr, res)
            return max(left, right) + 1

        count(root)
        return res

