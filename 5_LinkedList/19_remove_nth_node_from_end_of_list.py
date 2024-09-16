"""
Difficulty: Medium
Times Completed: 1
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
Basic Description:
    Given a linked list, remove the nth element from the end of the list
"""

from list_utils import ListNode, view_list, recursive_create
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        The idea is to maintain two pointers, one with a delay of n
        """

        slow, fast = head, head
        counter = 1
        while fast.next is not None:
            fast = fast.next
            if counter > n:
                slow = slow.next

            counter += 1

        if counter == n:
            to_delete = slow
            return to_delete.next
        else:
            to_delete = slow.next
            next_to_delete = to_delete.next
            slow.next = next_to_delete
            return head


if __name__ == "__main__":
    values = [1]
    n = 1
    head = recursive_create(values)
    new_head = Solution().removeNthFromEnd(head, n)
    view_list(new_head)
