class Solution:
    def generateTrees(self, n: int):
        if n == 0:
            return []

        def build_trees(start: int, end: int):
            trees = []
            if start > end:
                trees.append(None)
                return trees

            for root_val in range(start, end + 1):
                left_trees = build_trees(start, root_val - 1)
                right_trees = build_trees(root_val + 1, end)

                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(root_val)  # Use LeetCode’s TreeNode
                        root.left = l
                        root.right = r
                        trees.append(root)

            return trees

        return build_trees(1, n)
