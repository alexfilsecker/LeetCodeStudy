from tree_utils import TreeNode, build_binary_tree, get_nodes
from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recursive_invert(node: Optional[TreeNode]):
            if node is None:
                return
            left = node.left
            node.left = node.right
            node.right = left
            recursive_invert(node.left)
            recursive_invert(node.right)

        recursive_invert(root)
        return root


if __name__ == "__main__":
    root = [4, 2, 7, 1, 3, 6, 9]
    root_tree = build_binary_tree(root)
    new_root = Solution().invertTree(root_tree)
    nodes = get_nodes(new_root)
    print(nodes)
