"""medium"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def refactor(matrix, target):
            for row in matrix:
                first, last = row[0], row[-1]
                if target >= first and target <= last:
                    return row

            return False

        nums = refactor(matrix, target)
        if nums is False:
            return False

        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return True

            if nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return False


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = -2
    print(Solution().searchMatrix(matrix, target))
