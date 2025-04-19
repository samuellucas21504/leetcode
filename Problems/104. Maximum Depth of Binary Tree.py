# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def _recursion(node, d):
            if node is None:
                return d

            d += 1
            return max(_recursion(node.left, d), _recursion(node.right, d))

        return _recursion(root, 0)