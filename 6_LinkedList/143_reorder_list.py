"""
Difficulty: Medium
Times Completed: 2
Link: https://leetcode.com/problems/reorder-list/description/
Basic Description:
    Reorder a linked list in the order 0 -> n-1 -> 1 -> n-2 -> 2 -> n-3 ...
"""

from list_utils import ListNode, recursive_create, view_list
from typing import Optional


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        The aproach is divided in three steps:
        1. find the middle
        2. reverse the list from the middle to the end
        3. have two pointer, one from the head and the other from the end,
           and start to reorder the list
        """

        # Required minimum length of 3
        if head is None or head.next is None or head.next.next is None:
            return

        # 1. Find the middle
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        # 2. Reverse from the middle
        current = slow
        prev = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        # 3. Reorder the list
        right = prev
        left = head
        while right.next is not None and left.next is not None:
            next_left = left.next
            left.next = right
            left = left.next
            next_right = right.next
            left.next = next_left
            right = next_right
            left = left.next


if __name__ == "__main__":
    values = [1, 2, 3, 4]
    head = recursive_create(values)
    Solution().reorderList(head)
    print("\nSolution Done")
    view_list(head)
