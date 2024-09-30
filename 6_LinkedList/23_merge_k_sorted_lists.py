"""
Difficulty: Hard
Completed Times: 2
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


class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        The idea is to implement a monotonic list of nodes.
        At first we add all the heads, and sort them.
        Then we continiously do the following steps:

            1. pop the left most value, which is always going to be the
            minimum of the nodes in dispute
            2. append it to the tail of the resulting linked list
            3. insert the next node of the node we just poped in the correct order
        """
        filtered = [head for head in lists if head is not None]
        nodes = sorted(filtered, key=lambda x: x.val)

        tail = ListNode()
        result = tail
        while len(nodes) > 0:
            print(nodes)
            # Extract the smallest node
            smallest = nodes.pop(0)

            # Set the next node in the result to the smallest
            tail.next = smallest

            # Insert the node in nodes in the apropiate position
            next_node = smallest.next
            if next_node is not None:
                done = False
                # Since is probable that the new node's value is higher than
                # The others, we iterate on reverse
                for index in range(len(nodes) - 1, -1, -1):
                    competitor = nodes[index]
                    if next_node.val >= competitor.val:
                        nodes.insert(index + 1, next_node)
                        done = True
                        break

                if not done:
                    nodes.insert(0, next_node)

            tail = tail.next

        return result.next


if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    heads = [recursive_create(l) for l in lists]
    for head in heads:
        view_list(head)
    print("--------------------------\n")

    new_head = Solution2().mergeKLists(heads)
    # new_head = Solution().merge2Lists(heads[0], heads[1])
    view_list(new_head)
