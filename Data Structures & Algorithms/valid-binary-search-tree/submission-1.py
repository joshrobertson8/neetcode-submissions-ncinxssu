# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        is_left_valid = not root.left or self._isValidBST(root.left, float("-inf"), root.val)
        is_right_valid = not root.right or self._isValidBST(root.right, root.val, float("inf"))

        return is_left_valid and is_right_valid


    def _isValidBST(self, node, leftBound, rightBound):
        # take a range and if the node.val is strictly between it
        # continue, else immediately return false

        if not (leftBound < node.val < rightBound):
            return False

        is_left_valid = not node.left or self._isValidBST(node.left, leftBound, node.val)
        is_right_valid = not node.right or self._isValidBST(node.right, node.val, rightBound)

        return is_left_valid and is_right_valid