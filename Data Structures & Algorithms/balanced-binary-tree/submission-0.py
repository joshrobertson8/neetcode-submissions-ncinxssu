class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):

            if not node:
                return 0
  
            r, l = dfs(node.right), dfs(node.left)

            if r == -1 or l == -1:
                return -1

            if abs(r - l) > 1:
                return -1

            return 1 + max(r, l)

        return dfs(root) != -1