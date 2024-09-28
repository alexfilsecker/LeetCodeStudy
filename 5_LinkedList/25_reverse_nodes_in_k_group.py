"""
Dificulty: Hard
Completed Times: 1
Link: https://leetcode.com/problems/reverse-nodes-in-k-group/
Basic Description:
    Given a linked list, 1 -> 2 -> 3 -> 4 -> 5 and a number k
    reverse de list by groups of k. for example if k is 2 the 
    result should be
    2 -> 1 -> 4 -> 3 -> 5
    k is always going to be less or equal to the lenght of the list
    If the lenght of the list is not a multiple of k, leave
    the remaining nodes intact
"""

from list_utils import ListNode, recursive_create, view_list
from typing import Optional


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy
        while True:
            kth = self.getKth(group_prev, k)
            if not kth:
                break

            group_next = kth.next

            prev, curr = kth.next, group_prev.next

            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp

        return dummy.next

    def getKth(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1

        return curr


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]
    k = 2
    head = recursive_create(values)
    view_list(head)
    print("-------\n")
    new_head = Solution().reverseKGroup(head, k)
    view_list(new_head)
