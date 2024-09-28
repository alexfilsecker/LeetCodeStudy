"""
Dificulty: Medium
Times Completed: 1
Link: https://leetcode.com/problems/binary-tree-right-side-view/
Basic Description:
    From top to bottom return a list of the values of all the right side of a tree
"""

from typing import Optional, List
from tree_utils import build_binary_tree, TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        The idea is to do a level traverse of the tree, and append to result
        only the right most value in each level
        """

        if not root:
            return []

        result = []
        queue = [root]
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.pop(0)
                if i == level_size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result


if __name__ == "__main__":
    values = [1, 2, 3, None, 5, None, 4]
    root = build_binary_tree(values)
    print(Solution().rightSideView(root))
