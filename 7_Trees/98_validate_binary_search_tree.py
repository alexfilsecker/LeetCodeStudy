"""
Dificulty: Medium
Times Completed: 1
Link: https://leetcode.com/problems/validate-binary-search-tree/
Basic Description:
    Validate that a tree is a BST
"""

from typing import Optional
from tree_utils import TreeNode, build_binary_tree


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """The idea is to traverse in dfs while keeping the low and high boundaries"""

        def dfs(root: Optional[TreeNode], low_bound: int, high_bound: int) -> bool:
            if not root:
                return True

            return (
                root.val < high_bound
                and root.val > low_bound
                and dfs(root.left, low_bound, root.val)
                and dfs(root.right, root.val, high_bound)
            )

        return dfs(root, -(2**31) - 1, 2**31)


if __name__ == "__main__":
    values = [5, 4, 6, None, None, 3, 7]
    root = build_binary_tree(values)
    print(Solution().isValidBST(root))

#         5
#       4      6
#            3   7
#           a b c d
