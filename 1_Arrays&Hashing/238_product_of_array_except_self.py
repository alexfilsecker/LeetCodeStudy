"""
Dificulty: Medium
Times Completed: 2
Link: https://leetcode.com/problems/product-of-array-except-self/description/
Basic Description:
    Given nums, return an array in wich all every element is equal to the
    product of all other numbers except self. You must do it without division
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        We calculate a prefix list and a sufix list.
        prefix[i] is the product of all numbers before i
        and sufix[i] is the product of all numbers after i
        """
        n = len(nums)
        prefix = [1] * n
        sufix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            sufix[i] = sufix[i + 1] * nums[i + 1]

        return [prefix[i] * sufix[i] for i in range(n)]


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(Solution().productExceptSelf(nums))
