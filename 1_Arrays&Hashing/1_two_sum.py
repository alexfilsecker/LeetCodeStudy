"""easy"""


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num_left in enumerate(nums):
            sub_nums = nums[i + 1 :]
            for j, num_right in enumerate(sub_nums):
                if num_left + num_right == target:
                    return [i, j + i + 1]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))
