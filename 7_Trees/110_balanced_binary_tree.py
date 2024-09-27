"""
Dificulty: Easy
Times Completed: 1
Link: https://leetcode.com/problems/balanced-binary-tree/description/
Basic Description:
    Given a tree, see if it is height balanced

    A height-balanced binary tree is a binary tree in which the depth of
    the two subtrees of every node never differs by more than one.
"""

from tree_utils import TreeNode, build_binary_tree
from typing import Optional


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        balanced = [True]

        def dfs(root: Optional[TreeNode]) -> int:
            """Returns the height of a node"""
            print("visiting node", root)

            if root is None:
                return -1

            left_height = dfs(root.left)
            right_height = dfs(root.right)

            if balanced[0]:
                balanced[0] = abs(left_height - right_height) <= 1

            height = 1 + max(left_height, right_height)
            return height

        dfs(root)
        return balanced[0]


if __name__ == "__main__":
    values = [1, 2, 2, 3, 3, None, None, 4, 4]
    root = build_binary_tree(values)
    print(Solution().isBalanced(root))
