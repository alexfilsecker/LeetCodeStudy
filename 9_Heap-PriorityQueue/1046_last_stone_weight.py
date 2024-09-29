"""
Dificulty: Easy
Times Completed: 1
Link: https://leetcode.com/problems/last-stone-weight/description/
Basic Description:
    We go destroing stones, read description in link xd
"""

from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-1 * stone for stone in stones]
        heapify(max_heap)
        while len(max_heap) > 1:
            print(max_heap)
            y = heappop(max_heap)
            x = heappop(max_heap)
            if x != y:
                new_stone = y - x
                heappush(max_heap, new_stone)

        if len(max_heap) > 0:
            return -1 * max_heap[0]
        return 0


if __name__ == "__main__":
    stones = [2, 7, 4, 1, 8, 1]
    print(Solution().lastStoneWeight(stones))
