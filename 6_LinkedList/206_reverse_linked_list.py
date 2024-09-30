"""easy"""

from typing import List, Optional
from list_utils import ListNode, recursive_create, view_list


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
