"""
Dificulty: Medium
Times Completed: 1
Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
Basic Description:
    Count good nodes in a binary tree.
    A node is good if in the path from root to the node
    there are no nodes with a value grater than the node
"""

from tree_utils import TreeNode, build_binary_tree


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        The idea is to do a dfs that keeps track of the maximum value
        in the path.
        """
        res = [0]

        def dfs(root: TreeNode, max: int):
            if not root:
                return

            if root.val >= max:
                res[0] += 1
                max = root.val

            dfs(root.left, max)
            dfs(root.right, max)

        dfs(root, root.val)
        return res[0]


if __name__ == "__main__":
    values = [3, 1, 4, 3, None, 1, 5]
    root = build_binary_tree(values)
    print(Solution().goodNodes(root))
