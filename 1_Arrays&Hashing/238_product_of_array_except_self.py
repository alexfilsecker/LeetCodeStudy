"""medium"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        n = len(nums)
        result = [1] * n
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        for i in range(n - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(Solution().productExceptSelf(nums))
