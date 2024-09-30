"""
Dificulty: Hard
Times Completed: 1
Link: https://leetcode.com/problems/find-median-from-data-stream/description/
Basic Description:
    From a stream, queep track of the median
"""

from typing import List, Union
from heapq import heappush, heappop


class MedianFinder:
    """
    The idea is to use two heaps, one for the upper part of the median
    and other for the lower part.
    """

    def __init__(self):
        self.minHeapForLarge = []
        self.maxHeapForSmall = []

    def addNum(self, num: int) -> None:
        if len(self.maxHeapForSmall) == 0 or -1 * self.maxHeapForSmall[0] >= num:
            heappush(self.maxHeapForSmall, -1 * num)
        else:
            heappush(self.minHeapForLarge, num)

        # Balance the heaps:
        if len(self.maxHeapForSmall) > len(self.minHeapForLarge) + 1:
            heappush(self.minHeapForLarge, -1 * heappop(self.maxHeapForSmall))
        elif len(self.maxHeapForSmall) < len(self.minHeapForLarge):
            heappush(self.maxHeapForSmall, -1 * heappop(self.minHeapForLarge))

    def findMedian(self) -> float:
        if len(self.minHeapForLarge) == len(self.maxHeapForSmall):
            return (self.minHeapForLarge[0] + -1 * self.maxHeapForSmall[0]) / 2
        else:
            return -1 * self.maxHeapForSmall[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


def run(methods: List[str], args: List[List[str]]) -> List[Union[int, None]]:
    action_dict = {
        "MedianFinder": MedianFinder.__init__,
        "addNum": MedianFinder.addNum,
        "findMedian": MedianFinder.findMedian,
    }
    obj = MedianFinder(*args[0])
    result = [None]
    for i in range(1, len(methods)):
        method = methods[i]
        arg = args[i]
        result.append(action_dict[method](obj, *arg))

    return result


if __name__ == "__main__":
    methods = [
        "MedianFinder",
        "addNum",
        "findMedian",
        "addNum",
        "findMedian",
        "addNum",
        "findMedian",
        "addNum",
        "findMedian",
        "addNum",
        "findMedian",
        "addNum",
        "findMedian",
        "addNum",
        "findMedian",
        "addNum",
        "findMedian",
        "addNum",
        "findMedian",
        "addNum",
        "findMedian",
        "addNum",
        "findMedian",
    ]
    args = [
        [],
        [6],
        [],
        [10],
        [],
        [2],
        [],
        [6],
        [],
        [5],
        [],
        [0],
        [],
        [6],
        [],
        [3],
        [],
        [1],
        [],
        [0],
        [],
        [0],
        [],
    ]
    print(run(methods, args))
