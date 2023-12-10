"""medium"""

from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counter = Counter(nums)
        sorted_counter = sorted(num_counter.items(), key=lambda x: x[1], reverse=True)
        result = []
        for number, count in sorted_counter:
            result.append(number)
            if len(result) == k:
                return result


if __name__ == "__main__":
    nums = [3, 0, 1, 0]
    k = 1
    print(Solution().topKFrequent(nums, k))
