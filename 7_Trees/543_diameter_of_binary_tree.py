"""
Dificulty: Easy
Completed Times: 2
Link: https://leetcode.com/problems/diameter-of-binary-tree/description/
Basic Description:
    Given a Tree, return the diameter of it
    The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
    This path may or may not pass through the root.
"""

from typing import Optional
from tree_utils import TreeNode, build_binary_tree, get_nodes


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(root: Optional[TreeNode]) -> int:
            """
            Returns the height of a tree given its root. It also
            updates the res variable to the maximum diameter seen
            """

            if root is None:
                # The height of a None tree is -1 following convention
                return -1

            left_height = dfs(root.left)
            right_height = dfs(root.right)

            diameter = left_height + right_height + 2  # 2 because of the -1

            # Update the maximum diameter
            res[0] = max(res[0], diameter)

            # Calculate the height of the tree
            height = 1 + max(left_height, right_height)
            return height

        dfs(root)
        return res[0]


if __name__ == "__main__":
    values = [1, 2]
    root = build_binary_tree(values)
    print(Solution().diameterOfBinaryTree(root))
