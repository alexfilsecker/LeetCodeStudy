"""medium"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_count = 0
        while num_set:
            num = num_set.pop()
            count_down = 1
            while num - count_down in num_set:
                num_set.remove(num - count_down)
                count_down += 1
            count_down -= 1

            count_up = 1
            while num + count_up in num_set:
                num_set.remove(num + count_up)
                count_up += 1
            count_up -= 1

            count = 1 + count_up + count_down
            if count > max_count:
                max_count = count

        return max_count


if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    print(Solution().longestConsecutive(nums))
