"""
Dificulty: Easy 
Times Completed: 2
Link: https://leetcode.com/problems/contains-duplicate/description/
Basic Description:
    Check if an array of nums has a duplicated value
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Create a hash of nums to be able to check in O(1) if we have already
        seen that number. Then traverse all the list updating the hash
        """

        # A set is the same as a hash of { key: True }
        hash = set()

        for num in nums:
            if num in hash:
                return True
            else:
                hash.add(num)

        return False


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(Solution().containsDuplicate(nums))
