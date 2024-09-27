"""
Dificulty: Easy
Times Completed: 1
Link: https://leetcode.com/problems/subtree-of-another-tree/description/
Basic Description:
    See if sub tree is indeed a sub tree of a tree
"""

from typing import Optional
from tree_utils import TreeNode, build_binary_tree


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        if self.is_same(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def is_same(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            if p is None and q is None:
                return True

            return False

        return (
            p.val == q.val
            and self.is_same(p.left, q.left)
            and self.is_same(p.right, q.right)
        )


if __name__ == "__main__":
    root_values = [3, 4, 5, 1, 2]
    subroot_values = [4, 1, 2]
    root = build_binary_tree(root_values)
    subroot = build_binary_tree(subroot_values)
    print(Solution().isSubtree(root, subroot))
