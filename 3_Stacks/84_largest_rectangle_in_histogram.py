"""hard"""

from typing import List, Tuple


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack: List[Tuple[int, int]] = []
        max_area = 0
        for i, h in enumerate(heights):
            start = i
            while len(stack) > 0 and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, (i - index) * height)
                start = index
            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, (len(heights) - i) * h)

        return max_area


if __name__ == "__main__":
    heights = [0, 3, 2, 5]
    print(Solution().largestRectangleArea(heights))
