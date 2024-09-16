"""
Dificulty: Medium
Completed Times: 1
Link: https://leetcode.com/problems/find-the-duplicate-number/
Basic Description:
    An array nums of size n + 1, has numbers from 1 to n. So there is one duplicate
    Find that duplicate number without modifing nums and in O(1) space complexity
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        So in order to know how to solve this problem we must know the existance of
        floyds algorithm. That's the only way.

        So basically, we treat the list as a linked list, where the values represent the index
        of the next node. Then, as the list must has duplicates, it means that it has a cycle.
        Then we must utilize floyds algorithm to find the begining of the cycle which is
        the repeated number
        """

        # We first find the intersection of a fast and a slow pointer
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Then we find the begining of the cycle by placing another slow
        # pointer at the begining of the list and waiting for them to colide
        slow2 = nums[0]
        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow


if __name__ == "__main__":
    nums = [3, 1, 3, 4, 2]
    print(Solution().findDuplicate(nums))
