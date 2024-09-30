from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: "Optional[ListNode]" = next

    def __repr__(self):
        return f"Node = {self.val}"


def recursive_create(values: List[int], index: int = 0) -> ListNode:
    node = ListNode()
    node.val = values[index]
    if index < len(values) - 1:
        node.next = recursive_create(values, index + 1)

    return node


def add_cycle(head: ListNode, pos: int):
    cur = head
    counter = 0
    cycle_node = None
    while cur.next is not None:
        if counter == pos:
            cycle_node = cur
        cur = cur.next
        counter += 1

    cur.next = cycle_node


def view_list(head: ListNode):
    node = head
    node_list = []
    while True:
        # print(node)
        if node is None:
            break
        node_list.append(node.val)
        if node.next is None:
            break
        node = node.next

    print(node_list)
