"""
Dificulty: Medium
Times Completed: 1
Link: https://leetcode.com/problems/binary-tree-level-order-traversal/description/
Basic Description:
    given a tree, return a list of lists of the values, level by level, ie a bfs
"""

from typing import Optional, List
from tree_utils import TreeNode, build_binary_tree


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = [root]
        res = []
        while len(queue) > 0:
            new_queue = []
            level = []
            while len(queue) > 0:
                node = queue.pop(0)
                level.append(node.val)
                if node.left is not None:
                    new_queue.append(node.left)
                if node.right is not None:
                    new_queue.append(node.right)

            res.append(level)
            queue = new_queue.copy()

        return res


if __name__ == "__main__":
    values = [3, 9, 20, None, None, 15, 7]
    root = build_binary_tree(values)
    print(Solution().levelOrder(root))
