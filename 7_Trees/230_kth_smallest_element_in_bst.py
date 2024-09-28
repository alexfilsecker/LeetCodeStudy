"""
Dificulty: Medium
Times Completed: 1
Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
Basic Description:
    Given a bst, return the kth smallest element
"""

from typing import Optional
from tree_utils import TreeNode, build_binary_tree


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """The idea is to do a in order traversal"""
        result = []

        def inorder(root: Optional[TreeNode]):
            if not root:
                return

            inorder(root.left)
            result.append(root.val)
            if len(result) == k:
                return
            inorder(root.right)

        inorder(root)
        return result[k - 1]


if __name__ == "__main__":
    values = [3, 1, 4, None, 2]
    root = build_binary_tree(values)
    k = 2
    print(Solution().kthSmallest(root, k))
