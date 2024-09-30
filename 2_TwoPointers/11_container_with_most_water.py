"""hard"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_l, max_r = 0, 0
        trapped = 0
        index = left
        while left < right:
            left_v, right_v = height[left], height[right]
            max_l = max(max_l, left_v)
            max_r = max(max_r, right_v)
            water = min(max_l, max_r) - height[index]
            if water > 0:
                trapped += water
            if left_v <= right_v:
                left += 1
                index = left
            else:
                right -= 1
                index = right

        return trapped


if __name__ == "__main__":
    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(heights))
