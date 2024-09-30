"""medium"""

from typing import List, Set, Tuple


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ord = sorted(nums)
        print(ord)
        results: Set[Tuple[int]] = set()
        for i in range(len(ord) - 2):
            if i > 0 and ord[i] == ord[i - 1]:
                continue

            left, right = i + 1, len(ord) - 1
            while left < right:
                total = ord[i] + ord[left] + ord[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    results.add((ord[i], ord[left], ord[right]))
                    left += 1

        return [list(a) for a in results]


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    print(Solution().threeSum(nums))
