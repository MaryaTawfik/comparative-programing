# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode):
        result = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)       # 1. Visit left subtree
            result.append(node.val)  # 2. Visit root
            inorder(node.right)      # 3. Visit right subtree

        inorder(root)
        return result
