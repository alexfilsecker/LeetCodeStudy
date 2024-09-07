from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"Node = {self.val}"


def recursive_create(values: List[int], index: int = 0) -> ListNode:
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
