from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def recursive_create(values: List[int], index: int) -> ListNode:
    node = ListNode()
    node.val = values[index]
    if index < len(values) - 1:
        node.next = recursive_create(values, index + 1)

    return node


def view_list(head: ListNode):
    a = []

    def append_to_list(node: ListNode):
        print(node.val)
        a.append(node.val)
        if node.next is None:
            return
        append_to_list(node.next)

    append_to_list(head)
    print(a)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()

        def recursive_reverse(node: ListNode, new_head: ListNode) -> ListNode:
            print("visiting", node.val, node.next)
            if node.next is None:
                node.next = node
                new_head.val = node.val
                new_head.next = node.next
                return

            next = node.next
            node.next = node
            recursive_reverse(next, new_head)
            node.next = None

        recursive_reverse(head, new_head)
        print(new_head)

        view_list(new_head)


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]
    head = recursive_create(values, 0)
    view_list(head)
    print(Solution().reverseList(head))
    pass
