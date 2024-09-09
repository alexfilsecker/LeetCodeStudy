from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            # Check if we found the target
            if nums[mid] == target:
                return mid

            # Check if the left side (L -> M) is sorted
            if nums[left] <= nums[mid]:
                # Check if the target is in the left side
                if nums[left] <= target < nums[mid]:
                    right = mid - 1

                # Target is in the right side
                else:
                    left = mid + 1

            # The right part is sorted
            else:
                # Check if it is in the right side
                if nums[mid] < target <= nums[right]:
                    left = mid + 1

                # Target is in the left side
                else:
                    right = mid - 1

        return -1


if __name__ == "__main__":
    nums = [3, 1]
    target = 1
    print(Solution().search(nums, target))
