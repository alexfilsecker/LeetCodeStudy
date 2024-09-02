"""medium"""

import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low < high:
            k = (high + low) // 2
            time = sum([math.ceil(pile / k) for pile in piles])
            if time <= h:
                high = k

            elif time > h:
                low = k + 1

            else:
                high = k - 1

        return low


if __name__ == "__main__":
    piles = [3, 6, 7, 11]
    h = 8
    print(Solution().minEatingSpeed(piles, h))
