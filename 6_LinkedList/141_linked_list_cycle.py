"""easy"""

from list_utils import ListNode, recursive_create, add_cycle, view_list
from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            if fast == slow:
                return True

            fast = fast.next.next
            slow = slow.next

        return False


if __name__ == "__main__":
    nodes = [3, 2, 0, -4]
    head = recursive_create(nodes)
    pos = 1
    add_cycle(head, pos)
    print(Solution().hasCycle(head))
