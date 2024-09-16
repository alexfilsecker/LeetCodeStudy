"""
Dificulty: Medium
Times Completed: 1
Link: https://leetcode.com/problems/copy-list-with-random-pointer/description/
Basic Description:
    Given a linked list that apart from next has a random pointer on each node,
    Perform a deep copy of the list
"""

from typing import Optional, List, Union, Dict


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self):
        if self.random == None:
            return f"({self.val}, None)"
        else:
            return f"({self.val}, {self.random.val})"


def view_list(head: Optional[Node]):
    node = head
    node_list = []
    while node is not None:
        node_list.append(node)
        node = node.next

    print(node_list)


def create_list_with_random(values: List[List[Union[int, None]]]) -> Optional[Node]:
    def recursive_create(
        values: List[List[Union[int, None]]], map: Dict[int, Node], index=0
    ) -> Node:
        node = Node(values[index][0])
        map[index] = node
        if index < len(values) - 1:
            node.next = recursive_create(values, map, index + 1)

        return node

    map: Dict[int, Node] = dict()
    head = recursive_create(values, map)
    for index, value in enumerate(values):
        random_index = value[1]
        if random_index is not None:
            map[index].random = map[random_index]

    return head


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        """
        The idea here is to intertwine the lists in the way
        A -> A' -> B -> B' -> C -> C' ...
        Then we can point the random pointers correctly
        """

        # Trivial case
        if head is None:
            return None

        # Traverse the original list intertweaving it with a new list
        node = head
        while node is not None:
            next = node.next
            new_node = Node(node.val)
            node.next = new_node
            new_node.next = next
            node = next

        # Traverse the list again, for all the new nodes, the random value
        # will be the next of the random of the previous if it makes sense
        node = head
        while node is not None:
            copy = node.next
            if node.random is not None:
                copy.random = node.random.next

            node = copy.next

        # Separate the lists
        node = head
        new_head = node.next
        while node is not None:
            copy = node.next
            node.next = copy.next
            next = copy.next
            if next is not None:
                copy.next = next.next
            else:
                copy.next = None
            node = next

        return new_head


if __name__ == "__main__":
    values = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    head = create_list_with_random(values)
    new_head = Solution().copyRandomList(head)
    view_list(new_head)
