"""
Difficulty: Medium
Times Completed: 1
Link: https://leetcode.com/problems/reorder-list/description/
Basic Description:
    Reorder a linked list in the order 0 -> n-1 -> 1 -> n-2 -> 2 -> n-3 ...
"""

from list_utils import ListNode, recursive_create, view_list
from typing import Optional


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        The aproach is to store the linked list into a list and then
        pop from the left and right of it
        """

        # The linked list must at least of size 3 to actually have to do something
        if head is None or head.next is None:
            return

        # Store all nodes into a list
        nodes = []
        pointer = head
        while pointer is not None:
            nodes.append(pointer)
            pointer = pointer.next

        # Pop from the left, then right, then left until there is no more nodes
        i = 0
        pointer = nodes.pop(0)
        while len(nodes) > 0:
            if i % 2 == 0:
                pointer.next = nodes.pop()
            else:
                pointer.next = nodes.pop(0)

            i += 1
            pointer = pointer.next

        # Ensure that the last node is the last node
        pointer.next = None


if __name__ == "__main__":
    values = [1, 2]
    head = recursive_create(values)
    Solution().reorderList(head)
    view_list(head)
