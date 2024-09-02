"""medium"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        print(height)
        l, r = 0, len(height) - 1
        result = 0
        while l < r:
            total = min(height[l], height[r]) * (r - l)
            print(height[l], height[r], total)
            result = max(result, total)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return result


if __name__ == "__main__":
    height = [1, 3, 2, 5, 25, 24, 5]
    print(Solution().maxArea(height))
