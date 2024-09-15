"""
Difficulty: Medium
Times Completed: 1
Link: https://leetcode.com/problems/longest-consecutive-sequence/description/
Basic Description:
    Given an unsorted nums, return the lenght of the longest consecutive sequence
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        What we do is to create a set with all the numbers. Then we pop a random one
        and start poping all consecutive elements down of it and then all consecutive elements
        above of it while counting how many elements we have checked.
        """

        # Create the set of nums to eliminate duplicates.
        num_set = set(nums)

        max_count = 0
        while num_set:
            # Start with a random one
            num = num_set.pop()

            # See consecutive numbers below
            count_down = 1
            while num - count_down in num_set:
                num_set.remove(num - count_down)
                count_down += 1
            count_down -= 1

            # See consecutive numbers up
            count_up = 1
            while num + count_up in num_set:
                num_set.remove(num + count_up)
                count_up += 1
            count_up -= 1

            count = 1 + count_up + count_down  # 1 for the one we randomly picked

            # Evaluate max_count
            max_count = max(max_count, count)

        return max_count


if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    print(Solution().longestConsecutive(nums))
