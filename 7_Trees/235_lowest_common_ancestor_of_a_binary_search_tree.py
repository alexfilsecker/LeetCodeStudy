"""
Dificulty: Medium
Times Completed: 1
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
Basic Description:
    Given a Binary Search Tree (a tree that all left nodes are lower and all right are higher)
    find the lowest common ancestor of two nodes
"""

from tree_utils import TreeNode, build_binary_tree, find_in_bst


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        As it is a bst, if p and q values are less than root val,
        then both of them will be to the left, then we search to the left.
        We need to find the point where they are to different sides of root
        """
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                break

        return root


if __name__ == "__main__":
    values = [2, 1]
    root = build_binary_tree(values)
    p_value = 2
    q_value = 1
    p = find_in_bst(root, p_value)
    q = find_in_bst(root, q_value)
    print(Solution().lowestCommonAncestor(root, p, q))
