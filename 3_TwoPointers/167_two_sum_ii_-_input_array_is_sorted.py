"""medium"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while True:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l + 1, r + 1]

            if sum > target:
                r -= 1
            else:
                l += 1


if __name__ == "__main__":
    numbers = [3, 24, 50, 79, 88, 150, 345]
    target = 200
    print(Solution().twoSum(numbers, target))
