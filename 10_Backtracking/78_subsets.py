"""
Dificulty: Medium
Times Completed: 1
Link: https://leetcode.com/problems/subsets/description/
Basic Description:
    Return all the subsets of list of numbers
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def create_subset(index: int):
            if index == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[index])
            create_subset(index + 1)

            subset.pop()
            create_subset(index + 1)

        create_subset(0)
        return res


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().subsets(nums))
