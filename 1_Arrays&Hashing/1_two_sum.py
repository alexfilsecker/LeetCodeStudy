"""
difficulty: easy
completed times: 2
link: https://leetcode.com/problems/two-sum/description/
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {nums[i]: i for i in range(len(nums))}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash and hash[complement] != i:
                return [i, hash[target - num]]


if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6
    print(Solution().twoSum(nums, target))
