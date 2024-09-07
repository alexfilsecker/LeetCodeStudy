"""easy"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"Node = {self.val}"


def recursive_create(values: List[int], index: int) -> ListNode:
    node = ListNode()
    node.val = values[index]
    if index < len(values) - 1:
        node.next = recursive_create(values, index + 1)

    return node


def view_list(head: ListNode):
    node = head
    node_list = []
    while True:
        if node is None:
            break
        node_list.append(node.val)
        if node.next is None:
            break
        node = node.next

    print(node_list)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]
    head = recursive_create(values, 0)
    view_list(head)
    print(Solution().reverseList(head))
    pass
