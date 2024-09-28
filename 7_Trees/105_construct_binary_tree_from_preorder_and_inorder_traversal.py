"""
Dificulty: Medium
Times Completed: 1
Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
Basic Description:
    Given the preorder and inorder traversal, reconstruct the tree
"""

from typing import Optional, List
from tree_utils import TreeNode, get_nodes


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    root = Solution().buildTree(preorder, inorder)
    print(get_nodes(root))
