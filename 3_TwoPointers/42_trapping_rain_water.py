from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        print(height)
        left, right = 0, 1
        water = 0
        land = 0
        while left < len(height) - 1:
            print(height[left], height[right])
            if height[right] < height[left]:
                land += height[right]
                if right == len(height) - 1:
                    left += 1
                else:
                    right += 1
            else:
                plus = (right - left - 1) * min(height[left], height[right])
                print("plus", plus, "land", land, "result", plus - land)
                water += plus - land
                land = 0
                left = right
                right += 1

        return water


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(height))
