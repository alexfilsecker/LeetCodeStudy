"""easy"""

from typing import Optional
from list_utils import ListNode, recursive_create, view_list


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        head1, head2 = list1, list2
        while head1 is not None and head2 is not None:
            if head1.val > head2.val:
                curr.next = head2
                head2 = head2.next
            else:
                curr.next = head1
                head1 = head1.next

            curr = curr.next

        if head1 is None:
            curr.next = head2
        else:
            curr.next = head1

        return dummy.next


if __name__ == "__main__":
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    head1 = recursive_create(list1)
    head2 = recursive_create(list2)
    print(Solution().mergeTwoLists(head1, head2))
