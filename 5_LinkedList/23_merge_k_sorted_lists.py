"""
Difficulty: Hard
Completed Times: 1
Link: https://leetcode.com/problems/merge-k-sorted-lists/description/
Basic Description:
    Given k sorted linked lists, merge them all into one sorted linked list
"""

from list_utils import ListNode, view_list, recursive_create
from typing import Optional, List


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        The idea is to merge the lists secuentially. First the 1st and 2nd lists
        form the result, then the result and 3rd list form result and so on
        """
        heads = lists
        result = None
        for head in heads:
            result = self.merge2Lists(result, head)

        return result

    def merge2Lists(
        self, head1: Optional[ListNode], head2: Optional[ListNode]
    ) -> Optional[ListNode]:
        node1, node2 = head1, head2
        tail = ListNode()
        result = tail
        while node1 is not None or node2 is not None:
            # None of the nodes are None
            if node1 is not None and node2 is not None:
                if node1.val < node2.val:
                    tail.next = node1
                    node1 = node1.next
                else:
                    tail.next = node2
                    node2 = node2.next

            # node1 is not None but node2 is
            elif node1 is not None:
                tail.next = node1
                node1 = node1.next

            # node1 is None but node2 is not None
            else:
                tail.next = node2
                node2 = node2.next

            tail = tail.next

        return result.next


if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    heads = [recursive_create(l) for l in lists]
    for head in heads:
        view_list(head)
    print("--------------------------\n")

    new_head = Solution().mergeKLists(heads)
    # new_head = Solution().merge2Lists(heads[0], heads[1])
    view_list(new_head)
