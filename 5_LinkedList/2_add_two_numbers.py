"""
Difficulty: Medium
Completed Times: 1
Link: https://leetcode.com/problems/add-two-numbers/description/
Basic Description:
    Given two nums described by linked lists, return another linked list
    that represents the sum of the two numbers
"""

from typing import Optional
from list_utils import ListNode, recursive_create, view_list


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        The idea is to go advancing in each linked list at the same pace, adding the
        values together and creating a new list on the go
        """
        node1, node2 = l1, l2
        result = ListNode()
        result_head = result
        carry = 0
        while node1 is not None or node2 is not None:
            result.next = ListNode()
            result = result.next
            if node1 is not None and node2 is not None:
                sum = node1.val + node2.val + carry
            elif node1 is None:
                sum = node2.val + carry
            else:
                sum = node1.val + carry

            result.val = sum % 10
            carry = sum // 10

            # Advance node 1
            if node1 is not None:
                node1 = node1.next
            else:
                node1 = None
            # Advance node 2
            if node2 is not None:
                node2 = node2.next
            else:
                node2 = None

        if carry > 0:
            result.next = ListNode(carry)
        else:
            result = None
        return result_head.next


if __name__ == "__main__":
    values1 = [9, 9, 9, 9, 9, 9, 9]
    values2 = [9, 9, 9, 9]
    l1 = recursive_create(values1)
    l2 = recursive_create(values2)
    result = Solution().addTwoNumbers(l1, l2)
    view_list(result)
