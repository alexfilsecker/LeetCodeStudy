from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]


if __name__ == "__main__":
    nums = [5, 1, 2, 3, 4]
    print(Solution().findMin(nums))