"""
Dificulty: Hard
Times Completed: 1
Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
Basic description:
    Serialize a tree into a string and reconstruct the tree from the string
"""

from typing import Optional, List
from tree_utils import TreeNode, build_binary_tree


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        res = []

        def dfs(root: Optional[TreeNode]):
            if not root:
                res.append("N")
                return

            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        values = data.split(",")

        def dfs(values: List[str]) -> Optional[TreeNode]:
            val = values.pop(0)

            if val == "N":
                return None

            node = TreeNode(int(val))
            node.left = dfs(values)
            node.right = dfs(values)

            return node

        root = dfs(values)
        return root


if __name__ == "__main__":
    values = [1, 2, 3, None, None, 4, 5]
    root = build_binary_tree(values)

    serialized = Codec().serialize(root)
    Codec().deserialize(serialized)
