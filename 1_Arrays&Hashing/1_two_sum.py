"""
Difficulty: Easy
Times Completed: 2
Link: https://leetcode.com/problems/two-sum/description/
Basic Description:
    Return the two numbers in an array that sum a target number
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        The strategy is to hash the array in the form of "value: index". Then
        we traverse the array, calculating what is the complement needed for that
        number to be part of the result and we check if that complement is in
        our hash.
        """

        # Create the hash "value: index" for the array of nums
        hash = {nums[i]: i for i in range(len(nums))}

        # Traverse the array
        for i, num in enumerate(nums):

            # Calculate the complement
            complement = target - num

            # Check if that complement exists and it is not the same
            # number we are currently seing
            if complement in hash and hash[complement] != i:
                return [i, hash[target - num]]


if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6
    print(Solution().twoSum(nums, target))
