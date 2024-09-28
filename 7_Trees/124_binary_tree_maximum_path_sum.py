"""
Dificulty: Hard
Times Completed: 1
Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
Basic Description:
    A path, is a fucking path. Return the maximum sum of the nodes values for a path
"""

from tree_utils import TreeNode, build_binary_tree
from typing import Optional


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = [root.val]

        def dfs(root: Optional[TreeNode]) -> int:
            """
            Updates the result if the path pases through its node as the split
            and returns the maximum from considering the left or right as paths
            """

            if not root:
                return 0

            left_max = max(dfs(root.left), 0)
            right_max = max(dfs(root.right), 0)

            res[0] = max(res[0], root.val + left_max + right_max)

            return root.val + max(left_max, right_max)

        dfs(root)
        return res[0]


if __name__ == "__main__":
    values = [-10, 9, 20, None, None, 15, 7]
    root = build_binary_tree(values)
    print(Solution().maxPathSum(root))
