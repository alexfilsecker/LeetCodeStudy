"""
Dificulty: Medium
Times Completed: 1
Link: https://leetcode.com/problems/permutations/description/
Basic Description:
    Return all permutations of a list of nums
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """The idea is to simplify recursively the problem"""

        result = []

        # Base case when there are no nums to permute
        if len(nums) == 1:
            return [nums[:]]

        for _ in range(len(nums)):
            num = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(num)

            result.extend(perms)
            nums.append(num)

        return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().permute(nums))
