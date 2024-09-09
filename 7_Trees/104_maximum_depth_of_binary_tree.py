from tree_utils import TreeNode, build_binary_tree, get_nodes
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)


if __name__ == "__main__":
    values = [3, 9, 20, None, None, 15, 7]
    root = build_binary_tree(values)
    print(Solution().maxDepth(root))
