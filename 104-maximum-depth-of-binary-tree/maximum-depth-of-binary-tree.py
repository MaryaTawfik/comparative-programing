# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            len_left= dfs(node.left)
            len_right = dfs(node.right)
            maxdepth = max(len_left,len_right) + 1
            return maxdepth
        return dfs(root)
    
        
       

        