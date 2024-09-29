"""
Dificulty: Medium
Times Completed: 1
Link: https://leetcode.com/problems/k-closest-points-to-origin/description/
Basic Description:
    Given a list of points, return the k nearest to the origin
"""

from typing import List
from heapq import heapify, heappop


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [[point[0] ** 2 + point[1] ** 2, *point] for point in points]
        heapify(heap)
        res = []
        for _ in range(k):
            res.append(heappop(heap)[1:])

        return res


if __name__ == "__main__":
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    print(Solution().kClosest(points, k))
