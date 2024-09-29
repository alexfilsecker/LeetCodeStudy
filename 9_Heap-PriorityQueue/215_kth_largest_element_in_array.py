"""
Dificulty: Medium
Times Completed: 1
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
Basic Description:
    Return the kth largest element in an array without sorting the array
"""

from typing import List
from heapq import heapify, heappop


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        while len(nums) > k:
            heappop(nums)

        return nums[0]


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(Solution().findKthLargest(nums, k))
