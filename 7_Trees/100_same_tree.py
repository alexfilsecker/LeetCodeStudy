"""
Dificulty: Easy
Times Completed: 1
Link: https://leetcode.com/problems/same-tree/description/
Basic Description:
    Check if two trees are the same
"""

from typing import Optional
from tree_utils import TreeNode, build_binary_tree


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            if p is None and q is None:
                return True

            return False

        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )


if __name__ == "__main__":
    p_values = [1, 2, 3]
    q_values = [1, 2, 3]
    p = build_binary_tree(p_values)
    q = build_binary_tree(q_values)
    print(Solution().isSameTree(p, q))
