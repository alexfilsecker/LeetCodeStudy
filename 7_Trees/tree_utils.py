from typing import Optional, List, Union


# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        val=0,
        left: "Optional[TreeNode]" = None,
        right: "Optional[TreeNode]" = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        left_value = None
        right_value = None
        if self.left is not None:
            left_value = self.left.val
        if self.right is not None:
            right_value = self.right.val
        return f"val: {self.val}, left: {left_value}, right: {right_value}"


def build_binary_tree(nums: List[Union[None, int]]):
    if not nums:
        return None

    root = TreeNode(nums[0])
    queue = [root]

    i = 1
    while i < len(nums):
        node = queue.pop(0)

        if i < len(nums) and nums[i] is not None:
            node.left = TreeNode(nums[i])
            queue.append(node.left)
        i += 1

        if i < len(nums) and nums[i] is not None:
            node.right = TreeNode(nums[i])
            queue.append(node.right)
        i += 1

    return root


def get_nodes(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    nodes: List[int] = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        nodes.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return nodes


def find_in_bst(root: Optional[TreeNode], value: int) -> Optional[TreeNode]:
    if root is None:
        return None

    if root.val == value:
        return root

    if value > root.val:
        return find_in_bst(root.right, value)

    else:
        return find_in_bst(root.left, value)
