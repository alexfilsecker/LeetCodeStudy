"""easy"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = set()
        for num in nums:
            if num in hash:
                return True
            else:
                hash.add(num)

        return False


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(Solution().containsDuplicate(nums))
